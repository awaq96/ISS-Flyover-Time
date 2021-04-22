                                                                         
We will write a program that will take a list of lat and lon and display the time, in local time zones, when the ISS will be overhead next time at each of those locations. In addition, the program will print the number of people on ISS and their names.

For example, a user may provide a list of lat and lon in a file like this:

30.2672, -97.7431
29.7216, -95.3436
35.2220, -101.831
31.7619, -106.485
30.0802, -94.1266
32.7767, -96.7970

The program may output

30.2672, -97.7431: 11:15PM 
29.7216, -95.3436: 11:16PM
35.2220, -101.831: 11:17PM
31.7619, -106.485: 12:10PM
30.0802, -94.1266: 12:19PM
32.7767, -96.7970: 12:20PM

There are 4 people on ISS at this time:
firstname1 lastname1
firstname2 lastname2
firstname3 lastname3
firstname4 lastname4

The above is an example of the format of output, not the actual valid times or data.

We can find out the actual details by making a request to a webservice, like so:

http://api.open-notify.org/iss-pass.json?lat=29.721670&lon=-95.343631&n=1

http://api.open-notify.org/astros.json
                                                                         



