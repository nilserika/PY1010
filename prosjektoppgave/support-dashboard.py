# PY1010 - Prosjektoppgave vår 2025
# Support-dashboard
# Dette programmet leser inn data fra en Excel-fil og utfører ulike analyser på dataene.
#
# Nils Erik Asmundvaag

import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import math

file_path = 'support_uke_24.xlsx'

# Diverse hjelpemetoder
# Funksjon for å konvertere tidspunkt til timedelta
def parse_time(time_str):
    return timedelta(hours=int(time_str.split(':')[0]), minutes=int(time_str.split(':')[1]), seconds=int(time_str.split(':')[2]))

# Funksjon for å konvertere tidspunkt til time-objekt
def parse_time_of_day(time_str):
    return datetime.strptime(time_str, '%H:%M:%S').time()

# Funksjon for å regne ut gjennomsnittet av en liste med timedelta-objekter
def average_timedelta(td_list):
    total = sum(td_list, timedelta())
    return total / len(td_list)

# Funksjon for å formatere timedelta-objekter til streng
def format_timedelta(td):
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{hours:02}:{minutes:02}:{seconds:02}'


# Deloppgave a) Les inn Excel-filen og lagre dataene i arrayer
df = pd.read_excel(file_path)

# Initialize arrays
u_dag = []
kl_slett = []
varighet = []
score = []

u_dag = df['Ukedag'].values
kl_slett = [parse_time_of_day(time_str) for time_str in df['Klokkeslett'].values]
varighet = [parse_time(time_str) for time_str in df['Varighet'].values]
score = df['Tilfredshet'].values


# Deloppgave b) Finn antall henvendelser pr ukedag og lag et søylediagram

# Finn antall unike verdier og antall forekomster av hver verdi i u_dag
u_dag_counter = Counter(u_dag)

# Lag et søylediagram med henvenelser pr ukedag
labels, values = zip(*u_dag_counter.items())
plt.bar(labels, values)
plt.ylabel('Henvendelser')
plt.title('Antall henvendelser pr ukedag')
plt.show()


# Deloppgave c) Finn minste og lengste samtaletid

print("\nDeloppgave c) Finn minste og lengste samtaletid")

min_varighet = min(varighet)
max_varighet = max(varighet)
print("Minste samtaletid:", format_timedelta(min_varighet))
print("Lengste samtaletid:", format_timedelta(max_varighet))


# Deloppgave d) Finn gjennomsnittlig samtaletid

print("\nDeloppgave d) Finn gjennomsnittlig samtaletid")

avg_varighet = average_timedelta(varighet)
print("Gjennomsnittlig samtaletid:", format_timedelta(avg_varighet))


# Deloppgave e) Finn antall henvendelser i ulike tidsintervaller og lag et kakediagram

intervals = {
    '08-10': 0,
    '10-12': 0,
    '12-14': 0,
    '14-16': 0
}

# Tell antall henvendelser i de ulike tidsintervaller
for time in kl_slett:
    if time >= datetime.strptime('08:00:00', '%H:%M:%S').time() and time < datetime.strptime('10:00:00', '%H:%M:%S').time():
        intervals['08-10'] += 1
    elif time >= datetime.strptime('10:00:00', '%H:%M:%S').time() and time < datetime.strptime('12:00:00', '%H:%M:%S').time():
        intervals['10-12'] += 1
    elif time >= datetime.strptime('12:00:00', '%H:%M:%S').time() and time < datetime.strptime('14:00:00', '%H:%M:%S').time():
        intervals['12-14'] += 1
    elif time >= datetime.strptime('14:00:00', '%H:%M:%S').time() and time < datetime.strptime('16:00:00', '%H:%M:%S').time():
        intervals['14-16'] += 1

# Lag et kakediagram med antall henvendelser pr intervall
interval_labels = list(intervals.keys())
interval_values = list(intervals.values())

plt.pie(interval_values, labels=interval_labels, autopct=lambda p: f'{int(p * sum(interval_values) / 100)}', startangle=140)
plt.title('Antall henvendelser pr tidsintervall')
plt.show()


# Deloppgave f) Finn NPS-score

print("\nDeloppgave f) Finn NPS score")

# Tell antall score avgitt innenfor hvert intervall
score_intervals = {
    '1-6': 0,
    '7-8': 0,
    '9-10': 0
}

for s in score:
    if not math.isnan(s):
        if 1 <= s <= 6:
            score_intervals['1-6'] += 1
        elif 7 <= s <= 8:
            score_intervals['7-8'] += 1
        elif 9 <= s <= 10:
            score_intervals['9-10'] += 1

total_scores = sum(score_intervals.values())
pct_negatives = score_intervals['1-6'] / total_scores * 100
pct_neutrals = score_intervals['7-8'] / total_scores * 100
pct_positives = score_intervals['9-10'] / total_scores * 100
print(f"Totalt antall score gitt: {total_scores}")
print(f"Prosent negative score: {pct_negatives:.2f}")
print(f"Prosent nøytral score: {pct_neutrals:.2f}")
print(f"Prosent positiv score: {pct_positives:.2f}")
print(f"NPS-score: {(pct_positives - pct_negatives):.2f}")
