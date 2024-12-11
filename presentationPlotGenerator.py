from CellSpacer import runABM
#from differenceEquationApproximation import runApproximation

environmentUsed = "demonstration"

runABM(750, environmentUsed, [0.2, 0.4], environmentalAnimation=True, toPlot=True, toAnimate=True)
#runApproximation([10201, 0, 0, 0], 10000, environmentUsed, plot=True)