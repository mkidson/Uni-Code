def newBinEdges(arr, step):
    # this whole thing is just to combine the edge bins so they have at least 5 trials in
    tempBinEdges = np.arange(np.min(arr), np.max(arr), step)
    h, edges = np.histogram(arr, tempBinEdges)
    tempBinEdges=edges
    newLow=[edges[0],edges[1]]
    newHigh=[edges[-2],edges[-1]]

    done=False
    while not done:
        if h[0]<5:
            newLow[1]=edges[2]
            tempBinEdges=np.concatenate((newLow, tempBinEdges[3:]))

        if h[-1]<5:
            newHigh[0]=edges[-3]
            tempBinEdges=np.concatenate((tempBinEdges[:-3],newHigh))
                
        h, edges = np.histogram(arr, tempBinEdges)

        if h[0]>=5 and h[-1]>=5:
            done=True
    return edges    

step=1 # this changes depending on the mu, higher mu usually needs higher step
# gets bin edges from the function and then does np.histogram to get the data binned nicely
binEdges=newBinEdges(data, step)
histData, histBins=np.histogram(data, binEdges)

# finding the middles so that the plotting looks nice. i have to do weird things with the end bins because their width is non-standard but it should just work so don't worry about it
binMiddles=np.concatenate(([0.5*(histBins[1] + histBins[2])-step],0.5*(histBins[2:-1] + histBins[1:-2]),[0.5*(histBins[-3] + histBins[-2])+step]))

# so the xticks thing i've done is just for aesthetic purposes but i think it makes it look sick af
xTicks=np.concatenate(([f'$<${histBins[1]}'],[f'[{x},{x+step})' for x in histBins[1:-2]],[f'$\geq${histBins[-2]}']))

# i'm sure your plotting will work but this is just here as an example in case it doesn't
plt.errorbar(binMiddles, histData, np.sqrt(histData*(1-histData/N)), fmt='.', capsize=2, elinewidth=1)

# more aesthetic things
plt.xticks(binMiddles, xTicks)
