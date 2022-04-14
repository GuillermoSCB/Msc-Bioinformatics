from bioinformatica import BusquedaAproximadaPatron

patron="ATTCTGGA"
texto="CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC"
d=3
print(BusquedaAproximadaPatron(patron,texto, d))