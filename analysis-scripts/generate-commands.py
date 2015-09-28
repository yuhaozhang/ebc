num_datapoints = [1, 2, 3, 4, 5, 10, 25, 50, 75, 100]
data_types = ["gene-2d-iterations-0", "gene-2d-iterations-1", "gene-2d-iterations-2",
              "target-2d-iterations-0", "target-2d-iterations-1", "target-2d-iterations-2"]
names_methods = ["ebcranksum"]

print("# generated by generate-commands.py")
print("library(ROCR)")

print("results.final = {}")

# other methods
for dtype in data_types:
    dtypeR = dtype.replace("-", ".")
    for mname in names_methods:
        for ndat in num_datapoints:
            print("results = {}")
            print("for (file in list.files(\"/Users/Beth/Desktop/results-drug-%s/results-%d-%s\", full.names=TRUE)) {" % (dtype, ndat, mname))
            print("\tprint(file)")
            print("\td = read.delim(file, head = F)")
            print("\tnames(d) = c(\"entitypair\", \"cooccur\", \"pgkbstatus\")")
            print("\tpred = prediction(d$cooccur, d$pgkbstatus)")
            print("\tperf = unlist(slot(performance(pred, measure = \"auc\"), \"y.values\"))")
            print("\tresults = c(results, perf)")
            print("}")
            print("e = data.frame(mean(results > 0.7), mean(results > 0.8), mean(results > 0.9), median(results), min(results), max(results), %d, \"%s\", \"%s\")" % (ndat, dtypeR, mname))
            print("names(e) = c(\"fracg07\", \"fracg08\", \"fracg09\", \"median\", \"min\", \"max\", \"S\", \"datatype\", \"method\")")
            print("results.final = rbind(results.final, e)")