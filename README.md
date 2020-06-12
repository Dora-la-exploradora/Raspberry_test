# Raspberry_test
Raspberry Pi 4 heating report
by Daria Lunyova

June 12, 2020

ANNOTATION

To avoid the heating of electronic equipment during long work, people use fans. I examined the temperature change of the Raspberry Pi4 processor with/without additional cooling. To do this, I ran a program on the Raspberry Pi 4, which creates an artificial workload. We measured the temperature and frequency of the processor and then built graphs.
Overall, my results show that if you use cooling, the temperature of the processor will be much lower. This will allow Raspberry Pi 4 to keep its maximum CPU frequency for longer.

INTRODUCTION

Everybody knows that any electronic device begins to heat up during a long work under heavy load.
I chose this topic for my report because we use Raspberry Pi 4 in our project [1]. We installed a neuromodule on the Raspberry Pi 4 to detect objects in real-time. However, the detection speed slows down during a long work.
In this experiment, we checked how much additional cooling decreases the temperature of the processor. Because our fan was small and does not seem so efficient, I expected a little influence on the temperature.

METHODS

First, I measured the temperature of the processor without load. Then I ran a CPU stress-testing utility "stress-ng" which puts a lot of load on all the processor cores. Additionally, I launched "glxgears". This is a tool that loads the GPU. Both utilities work for ten minutes at the same time. After that, the Raspberry Pi is cooled for several minutes. The "vcgencmd measure_temp" command records the temperature. Then a graph is built using the data collected. See the repository on the Github for more details.

RESULTS

There are areas on the graphs where the system works without load. These are the first 60 seconds of operation and the last 120 seconds (the system cools down).
If you use only passive cooling, then the temperature of the processor rises to 85 degrees (fig. 1). On the other hand, the maximum temperature will be only 60 degrees with a fan (fig. 2).
Also, the heating time is very important. It took about 120 seconds for the second system to heat up to 60 degrees (fig. 2). The temperature of the first system reached 60 degrees in less than 50 seconds (fig. 1).

DISCUSSION

The results did not confirm my assumption that additional cooling does not greatly affect the temperature of the processor. 
People use fans as extra cooling because it significantly reduces the temperature of the CPU. Without a fan, the general heating temperature is 25 degrees higher, the heating rate is 2 times faster.
Thus, using only passive cooling is not enough to protect the processor from overheating.

Reference list

1. https://trello.com/b/Qgs68dGV/%D0%BF%D0%BE%D0%BC%D0%B8%D1%80%D1%81

Fig. 1. Thermal test. Passive cooling.
 
Fig. 2. Thermal test. Passive and active cooling.
