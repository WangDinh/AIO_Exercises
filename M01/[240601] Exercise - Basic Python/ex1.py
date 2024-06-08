def cal_classification_metric(tp, fp, fn):
    if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fn, int):
        print("Input values must be integers.")
        return

    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return
    
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * precision * recall / (precision + recall)
    
    print("Precision: ", precision)
    print("Recall: ", recall)
    print("F1: ", f1)

cal_classification_metric(2, 3, 4)