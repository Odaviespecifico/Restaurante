import csv
from Uteis import *


exibir_mesa(mesas,5)

writedict('mesa.csv',mesas,('Número','Capacidade','Status',"Pessoas"))