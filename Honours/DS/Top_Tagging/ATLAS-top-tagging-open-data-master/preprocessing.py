"""

######################### ATLAS Top Tagging Open Data ##########################

preprocessing.py - This script defines two functions. One applies a standard
pre-processing scheme to the constituent inputs, and the other standardizes the
high level quantity inputs. These functions are applied in script train.py

For a description of the pre-processing and resulting distributions, see
(*CDS pub note link*).

Author: Kevin Greif
Last updated 4/21/2022
Written in python 3

################################################################################

"""

# Numerical imports
import numpy as np


def constituent(data_dict, max_constits):
    """ constituent - This function applies a standard preprocessing to the
    jet data contained in train_dict. It will operate on the raw constituent
    level quantities and return 7 constituent level quantities which can be
    used for tagger training.

    Arguments:
    data_dict (dict of np arrays) - The python dictionary containing all of
    the constituent level quantities. Standard naming conventions will be
    assumed.
    max_constits (int) - The maximum number of constituents to consider in
    preprocessing. Cut jet constituents at this number.

    Returns:
    (np array) - The seven constituent level quantities, stacked along the last
    axis.
    """

    ############################## Load Data ###################################

    # Pull data from data dict
    pt = data_dict['fjet_clus_pt'][:,:max_constits]
    eta = data_dict['fjet_clus_eta'][:,:max_constits]
    phi = data_dict['fjet_clus_phi'][:,:max_constits]
    energy = data_dict['fjet_clus_E'][:,:max_constits]

    # Find location of zero pt entries in each jet. This will be used as a
    # mask to re-zero out entries after all preprocessing steps
    mask = np.asarray(pt == 0).nonzero()

    ########################## Angular Coordinates #############################

    # 1. Center hardest constituent in eta/phi plane. First find eta and
    # phi shifts to be applied
    eta_shift = eta[:,0]
    phi_shift = phi[:,0]

    # Apply them using np.newaxis
    eta_center = eta - eta_shift[:,np.newaxis]
    phi_center = phi - phi_shift[:,np.newaxis]

    # Fix discontinuity in phi at +/- pi using np.where
    phi_center = np.where(phi_center > np.pi, phi_center - 2*np.pi, phi_center)
    phi_center = np.where(phi_center < -np.pi, phi_center + 2*np.pi, phi_center)

    # 2. Rotate such that 2nd hardest constituent sits on negative phi axis
    second_eta = eta_center[:,1]
    second_phi = phi_center[:,1]
    alpha = np.arctan2(second_phi, second_eta) + np.pi/2
    eta_rot = (eta_center * np.cos(alpha[:,np.newaxis]) +
               phi_center * np.sin(alpha[:,np.newaxis]))
    phi_rot = (-eta_center * np.sin(alpha[:,np.newaxis]) +
               phi_center * np.cos(alpha[:,np.newaxis]))

    # 3. If needed, reflect so 3rd hardest constituent is in positive eta
    third_eta = eta_rot[:,2]
    parity = np.where(third_eta < 0, -1, 1)
    eta_flip = (eta_rot * parity[:,np.newaxis]).astype(np.float32)
    # Cast to float32 needed to keep numpy from turning eta to double precision

    # 4. Calculate R with pre-processed eta/phi
    radius = np.sqrt(eta_flip ** 2 + phi_rot ** 2)

    ############################# pT and Energy ################################

    # Take the logarithm, ignoring -infs which will be set to zero later
    log_pt = np.log(pt)
    log_energy = np.log(energy)

    # Sum pt and energy in each jet
    sum_pt = np.sum(pt, axis=1)
    sum_energy = np.sum(energy, axis=1)

    # Normalize pt and energy and again take logarithm
    lognorm_pt = np.log(pt / sum_pt[:,np.newaxis])
    lognorm_energy = np.log(energy / sum_energy[:,np.newaxis])

    ########################### Finalize and Return ############################

    # Reset all of the original zero entries to zero
    eta_flip[mask] = 0
    phi_rot[mask] = 0
    log_pt[mask] = 0
    log_energy[mask] = 0
    lognorm_pt[mask] = 0
    lognorm_energy[mask] = 0
    radius[mask] = 0

    # Stack along last axis
    features = [eta_flip, phi_rot, log_pt, log_energy,
                lognorm_pt, lognorm_energy, radius]
    stacked_data = np.stack(features, axis=-1)

    return stacked_data


def high_level(data_dict):
    """ high_level - This function "standardizes" each of the high level
    quantities contained in data_dict (subtract off mean and divide by
    standard deviation).

    Arguments:
    data_dict (dict of np arrays) - The python dictionary containing all of
    the high level quantities. No naming conventions assumed.

    Returns:
    (array) - The high level quantities, stacked along the last dimension.
    """

    # Empty list to accept pre-processed high level quantities
    features = []

    # Loop through quantities in data dict
    for quant in data_dict.values():

        # Some high level quantities have large orders of magnitude. Can divide
        # off these large exponents before evaluating mean and standard
        # deviation
        if 1e5 < quant.max() <= 1e11:
            # Quantity on scale TeV (sqrt{d12}, sqrt{d23}, ECF1, Qw)
            quant /= 1e6
        elif 1e11 < quant.max() <= 1e17:
            # Quantity on scale TeV^2 (ECF2)
            quant /= 1e12
        elif quant.max() > 1e17:
            # Quantity on scale TeV^3 (ECF3)
            quant /= 1e18

        # Calculated mean and standard deviation
        mean = quant.mean()
        stddev = quant.std()

        # Standardize and append to list
        standard_quant = (quant - mean) / stddev
        features.append(standard_quant)

    # Stack quantities and return
    stacked_data = np.stack(features, axis=-1)

    return stacked_data
