from differenceEquationApproximation import runApproximation

initialPops = [5101,
                      0,
                      5100,
                      0]



finalYellow, finalGreen = runApproximation(initialPops, 1000, "quasibrownian", plot = True)

print(f"Final Yellow Num = {finalYellow}")
print(f"Final Green Num = {finalGreen}")