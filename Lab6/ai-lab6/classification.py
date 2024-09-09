class Classification:

    def __init__(self, real, computed, labels):
        self.labelNames = labels
        self.realLabels = real
        self.computedLabels = computed

    def eval(self):
        TP = {}
        FP = {}
        TN = {}
        FN = {}
        for label in self.labelNames:
            TP[label] = sum(
                [1 if (self.realLabels[i] == label and self.computedLabels[i] == label) else 0 for i in range(len(
                    self.realLabels))])
            FP[label] = sum(
                [1 if (self.realLabels[i] != label and self.computedLabels[i] == label) else 0 for i in range(len(
                    self.realLabels))])
            TN[label] = sum(
                [1 if (self.realLabels[i] != label and self.computedLabels[i] != label) else 0 for i in range(len(
                    self.realLabels))])
            FN[label] = sum(
                [1 if (self.realLabels[i] == label and self.computedLabels[i] != label) else 0 for i in range(len(
                    self.realLabels))])

        return TP, FP, TN, FN

    def accuracy(self):
        return sum([1 if self.realLabels[i] == self.computedLabels[i] else 0 for i in range(0, len(
            self.realLabels))]) / len(self.realLabels)

    def precission(self, TP, FP):
        precision = {}
        for label in self.labelNames:
            precision[label] = TP[label] / (TP[label] + FP[label])
        return precision

    def recall(self, TP, FN):
        recall = {}
        for label in self.labelNames:
            recall[label] = TP[label] / (TP[label] + FN[label])
        return recall