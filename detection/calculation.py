# TODO
# 인화성 물질
# 고양이 멍멍이
# 우선순위 - 위험도 (인간 가중치)
# 물건 대비 위험도
class Calc:
    flammable_items = {'bicycle': 3, 'bench': 5, 'backpack': 8, 'umbrella': 9, 'handbag': 6, 'tie': 8, 'suitcase': 6,
                       'frisbee': 7, 'sports ball': 6, 'kite': 9, 'baseball bat': 5, 'baseball glove': 5,
                       'skateboard': 6, 'tennis racket': 5, 'bottle': 3, 'wine glass': 1, 'cup': 4, 'fork': 2,
                       'knife': 1, 'spoon': 2, 'bowl': 2, 'banana': 3, 'apple': 3, 'sandwich': 3, 'orange': 3,
                       'broccoli': 3, 'carrot': 3, 'hot dog': 3, 'pizza': 3, 'donut': 3, 'cake': 3, 'chair': 5,
                       'sofa': 7, 'pottedplant': 3, 'bed': 9, 'diningtable': 5, 'tvmonitor': 7, 'laptop': 7, 'mouse': 7,
                       'remote': 7, 'keyboard': 7, 'cell phone': 7, 'microwave': 7, 'oven': 7, 'toaster': 7, 'sink': 1,
                       'refrigerator': 7, 'book': 10, 'clock': 5, 'vase': 1, 'scissors': 1, 'teddy bear': 10,
                       'hair drier': 7, 'toothbrush': 5}

    important_items = {'person': 10, 'bird': 8, 'cat': 9, 'dog': 9, 'cow': 9, 'elephant': 8}

    fh = {'fire hydrant': -100}

    def flame_score(self,all_items):
        score = 0

        for item in all_items:
            score += Calc.flammable_items[item]
        return score

    def importance_score(self,all_items):
        score = 0
        for item in all_items:
            score += Calc.important_items[item]
        return score

    def test(self, case_num):
        import random

        flammable = list(Calc.flammable_items.keys())
        important = list(Calc.important_items.keys())
        flame_list = []
        imp_list = []

        for i in range(case_num):
            print("Flammable items: ",end="")
            for j in range(random.randint(0,len(flammable)-1)):
                rand_item = flammable[random.randint(0, len(flammable)-1)]
                print(rand_item, end=", ")
                flame_list.append(rand_item)
            print("\nImportant items: ",end="")
            for j in range(random.randint(0,len(important)-1)):
                rand_item = important[random.randint(0, len(important)-1)]
                print(rand_item, end=", ")
                imp_list.append(rand_item)

            print(f"\n\nFlammable score : {Calc.flame_score(0,flame_list)}",end="")
            print(f"\nImportance score : {Calc.importance_score(0,imp_list)}\n")


if __name__ == "__main__":
    import sys
    print("Input test case num : ",end="")
    test_case_num = int(sys.stdin.readline())

    Calc.test(0,test_case_num)


