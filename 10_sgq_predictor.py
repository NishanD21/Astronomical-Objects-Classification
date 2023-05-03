from skyndo.predict import predictor
import pandas as pd

alpha_coordinate = input("alpha: ")
delta_coordinate = input("delta: ")
u_band = input("u: ")
g_band = input("g: ")
r_band = input("r: ")
i_band = input("i: ")
z_band = input("z: ")
redshift_s = input("redshift: ")


prediction = predictor(alpha=float(alpha_coordinate), delta=float(delta_coordinate), u=float(u_band), g=float(g_band),
                        i=float(i_band), r=float(r_band), z=float(z_band), redshift=float(redshift_s))

print(f'Prediction: {prediction}')