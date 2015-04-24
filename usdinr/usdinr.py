print "d <- read.csv(\"usdinr.csv\", header=TRUE, sep=\",\");"
print "quartz();"
for i in range(1,6001): print "barplot(d$USD.INR[%d:%d]);" %(i,i+49)
