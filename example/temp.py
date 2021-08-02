    ## zip指標的標記
    for sentence, sentence_ws, sentence_pos, sentence_ner in zip(text, ws, pos, ner):
        #print(pos)
        pack_ws_pos_sentece(sentence_ws, sentence_pos)
        #-----------------------#
    sort_key.append(Counter(self_list).most_common(20))
    sort_words.append(Counter(common_list).most_common(20))
    print(name[i])
    print("done")
    #print(sentence)
    print("-----weighting-------")
#     print(sort_key[i])
#     print("------------")
#     print(sort_words[i])
    weight=[]
    for words in sort_words[i]:
        _TF=(words[1]/len(pos)) 
        _IDF=math.log(words[1]/sent_cnt)
        print(words[0])
        print(abs(_TF*_IDF))
        print()
        weight=zip(words[0],abs(_TF*_IDF))
    
    # for entity in sentence_ner:
    print(weight)
    print("----storing------")
