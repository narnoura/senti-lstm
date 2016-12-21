import os
import codecs
import sys
from optparse import OptionParser

# Evaluate accuracy for labels

class Evaluate:
    @staticmethod
    def parse_options():
        parser = OptionParser()
        parser.add_option('--gold', dest='gold_file', help='gold file', metavar='FILE')
        parser.add_option('--predicted', dest='predicted_file', help='predicted file', metavar='FILE')
        return parser.parse_args()

    def read_labels(self,file):
        labels = []
        tf = codecs.open(os.path.abspath(file), 'r')
        for row in tf:
            l = row.strip().split('\t')[1]
            labels.append(l)
            #labels.add(row.strip().split('\t')[1])
        tf.close()
        return labels

    def evaluate(self,gold,predicted):
        accuracy = 0
        err = 0
        i = 0
        for g in gold:
            pred = predicted[i]
            if pred == g:
                accuracy +=1
            else:
                err+=1
                #print g,pred
            i+=1
        print "correct",accuracy
        print "err",err
        accuracy = float(accuracy)/len(gold)
        return accuracy


if __name__ == '__main__':
    (options,args) = Evaluate.parse_options()
    e = Evaluate()
    if options.gold_file == 'None':
        sys.exit('no gold file specified')
    if options.predicted_file == 'None':
        sys.exit('no predicted file specified')
    print "gold file:" + options.gold_file
    print "predicted file:" + options.predicted_file
    gold = e.read_labels(options.gold_file)
    predicted = e.read_labels(options.predicted_file)
    accuracy = e.evaluate(gold,predicted)
    print "accuracy:",accuracy