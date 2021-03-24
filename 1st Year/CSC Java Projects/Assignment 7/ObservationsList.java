import java.lang.Iterable;
import java.util.*;

/**
 * ObservationsList
 */
public class ObservationsList implements Iterable<Observation> {

    private List<Observation> observationsList;

    public ObservationsList() {

        observationsList = new ArrayList<Observation>();
    }

    public void record(Observation observation) {

        observationsList.add(observation);
    }

    public void record(Registration reg, Time time) {

        observationsList.add(new Observation(reg, time));
    }

    public int getTotal() {

        return observationsList.size();
    }

    public List<Registration> getVehicles() {

        ArrayList<Registration> regs = new ArrayList<Registration>();
        for (Observation i : observationsList) {
            if (!regs.contains(i.getIdentifier())) {
                regs.add(i.getIdentifier());
            }
        }

        return regs;
    }

    public ObservationsList getObservations(final Registration identifier) {

        ObservationsList obsList = new ObservationsList();

        for (Observation obs : this.observationsList) {
            if (obs.isFor(identifier)) {

                obsList.record(obs);
            }
        }

        return obsList;
    }

    public ObservationsList getObservations(final Time s, final Time e) {

        ObservationsList obsList = new ObservationsList();

        for (Observation obs : this.observationsList) {
            if (obs.inPeriod(s, e)) {

                obsList.record(obs);
            }
        }

        return obsList;
    }

    public Iterator<Observation> iterator() {

        Collections.sort(observationsList);
        return observationsList.iterator();
    }
}