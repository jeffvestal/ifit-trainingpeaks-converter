#! /usr/bin/env python

import sys
inputFile = sys.argv[1]
print('processing %s' % inputFile)

sf = inputFile.split('.csv')
convertedFile = sf[-2] + '-converted' + '.csv'
print('writing converd output to %s' % convertedFile)

# I'm lazy right now
# 0 Time, 1 Miles, 2 MPH, 3 Watts, 4 HR, 5 RPM, 6 Resistance, 7 Relative Resistance, 8 Incline
newHeader = ['Minutes', 'Torq (N-m)','Km/h','Watts','Km','Cadence','Hrate','ID']
# no readings for these
torq = 0
idv = 22

#print (','.join(newHeader))

with open(inputFile) as f:
    with open(convertedFile, 'w') as c:
        c.write('%s\n' % ','.join(newHeader))
        for line in f:
            if line.startswith('Stages_Data') or line.startswith('English') or line.startswith('Time'):
                continue
            else:
                line = line.strip().split(',')
                sec,mins = line[0].split(':')
                deciTime = int(sec) + round(int(mins) / 60, 2)

                km = round(float(line[1]) * 1.60934, 5)
                kmph = round(float(line[2]) * 1.60934, 4)

                watts = int(line[3])
                cadence = int(line[5])
                try:
                    hr = int(line[4])
                except ValueError as e:
                    hr = int(float(line[4]))

                row = ','.join([str(v) for v in (deciTime, torq, kmph, watts, km, cadence, hr, idv)])
                c.write('%s\n' % row)

