### PROOF OF WORK ###
sid = 500481905
name = "Ethan Susanto"

# Extract first two digits of sid #
# convert to a string and extract #
temp_sid = str(sid)
repeats = int(temp_sid[:2])

# Repeat name as many times as above #
count = 1
while (count<=repeats) :
    print(name + " : {}".format(count))
    count = count+1
