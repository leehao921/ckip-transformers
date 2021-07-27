#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from ckip_transformers import __version__
from ckip_transformers.nlp import CkipWordSegmenter, CkipPosTagger, CkipNerChunker


def main():

    # Show version
    print(__version__)

    # Initialize drivers
    print("Initializing drivers ... WS")
    ws_driver = CkipWordSegmenter(level=1)
    print("Initializing drivers ... POS")
    pos_driver = CkipPosTagger(level=1)
    print("Initializing drivers ... NER")
    ner_driver = CkipNerChunker(level=1)
    print("Initializing drivers ... done")
    print()

    # Input text
    text = [
      "1.一種支付系統，包括： 一設定介面，設置於一行動裝置，用以設定對應於多個支付帳號的多個帳號關鍵字； 一關鍵字識別模組，用以接收該些帳號關鍵字，並依據一音頻信號識別出該些帳號關鍵字的其中之一以及多個操作關鍵字的其中之一；以及 一條碼產生模組，耦接於該關鍵字識別模組，用以依據該些帳號關鍵字的其中之一以及該些操作關鍵字的其中之一產生一支付條碼， 其中該行動裝置顯示該支付條碼執行一交易操作。2.如申請專利範圍第1項所述的支付系統，其中該條碼產生模組還用以依據該些帳號關鍵字的一第一帳號關鍵字以及該些操作關鍵字的一第一操作關鍵字產生對應於該第一帳號關鍵字以及該第一操作關鍵字的該支付條碼。3.如申請專利範圍第2項所述的支付系統，其中對應於該第一帳號關鍵字以及該第一操作關鍵字的該支付條碼被顯示時，該支付條碼被掃描以對該第一支付帳號執行對應於該第一操作關鍵字的該交易操作。4.如申請專利範圍第1項所述的支付系統，其中該交易操作是對該些支付帳號的其中之一執行收款操作以及付款操作的其中之一。5.如申請專利範圍第1項所述的支付系統，其中該些操作關鍵字的其中之一對應於收款操作以及付款操作的其中之一。6.如申請專利範圍第1項所述的支付系統，其中該關鍵字識別模組以及該條碼產生模組的至少其中之一被設置在該行動裝置。7.一種支付方法，適用於藉由一行動裝置執行一交易操作，其中該支付方法包括： 設定對應於多個支付帳號的多個帳號關鍵字； 接收一音頻信號，並依據該音頻信號識別出該些帳號關鍵字的其中之一以及多個操作關鍵字的其中之一； 依據該些帳號關鍵字的其中之一以及該些操作關鍵字的其中之一產生一支付條碼；以及 藉由該行動裝置顯示該支付條碼以執行一交易操作。8.如申請專利範圍第7項所述的支付方法，其中依據該些帳號關鍵字的其中之一以及該些操作關鍵字的其中之一產生該支付條碼的步驟包括： 依據該些帳號關鍵字的一第一帳號關鍵字以及該些操作關鍵字的一第一操作關鍵字產生對應於該第一帳號關鍵字以及該第一操作關鍵字的該支付條碼。9.如申請專利範圍第8項所述的支付方法，其中藉由該行動裝置顯示該支付條碼以執行該交易操作的步驟包括： 掃描對應於該第一帳號關鍵字以及該第一操作關鍵字的該支付條碼以對該第一支付帳號執行對應於該第一操作關鍵字的該交易操作。10.如申請專利範圍第7項所述的支付方法，其中該交易操作是對該些支付帳號的其中之一執行收款操作以及付款操作的其中之一。11.如申請專利範圍第7項所述的支付方法，還包括： 設定對應於收款操作以及付款操作的該些操作關鍵字。"
    ]

    # Run pipeline
    print("Running pipeline ... WS")
    ws = ws_driver(text)
    print("Running pipeline ... POS")
    pos = pos_driver(ws)
    print("Running pipeline ... NER")
    ner = ner_driver(text)

    print("Running pipeline ... done")

    print()

    # Show results
    for sentence, sentence_ws, sentence_pos, sentence_ner in zip(text, ws, pos, ner):
        print(sentence)
        print(pack_ws_pos_sentece(sentence_ws, sentence_pos))
        for entity in sentence_ner:
            print(entity)
        print()


# Pack word segmentation and part-of-speech results
def pack_ws_pos_sentece(sentence_ws, sentence_pos):
    assert len(sentence_ws) == len(sentence_pos)
    res = []
    for word_ws, word_pos in zip(sentence_ws, sentence_pos):
        res.append(f"{word_ws}({word_pos})")
    return "\u3000".join(res)


if __name__ == "__main__":
    main()
