# -*- coding: utf-8 -*-

import random

# 预设地区:
import re

# codelist = ["110000 ","120000 ","130000 ","140000","110107","420117","420200","420202","420203","420204","420205","420222"]    #随便设置了几个地区，基本都是湖北和北京的；

# 全国
# codelist = ["110000","120000","130000","140000","150000","210000","220000","230000","310000","320000","330000","340000","350000",
#             "360000","370000","410000","420000","430000","440000","450000","460000","510000","520000","530000","540000","500000",
#             "610000","620000","630000","640000","650000","710000","810000","820000"]

# 南京秦淮区
codelist = ["320104"]

weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
             '10': '2'}  # 校验码映射

# 大众化姓氏
Xing = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗" \
       "毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平" "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄危江童颜郭梅盛林刁" \
       "钟徐邱骆高夏蔡田胡凌霍万柯卢莫房缪干解应宗丁宣邓郁单杭洪包诸左石崔吉" "龚程邢滑裴陆荣翁荀羊甄家封芮储靳邴松井富乌焦巴弓牧隗山谷车侯伊宁仇祖武符" \
       "刘景詹束龙叶幸司韶黎乔苍双闻莘劳逄姬冉宰桂牛寿通边燕冀尚农温庄晏瞿茹习鱼容向古戈终居衡步都耿满弘国文东殴沃曾关红游盖益桓公晋楚闫"
Ming = '中笑贝凯歌易仁器义礼智信友上都卡被好无九加电金马钰玉忠孝秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香' \
       '月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭' \
       '冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽'


def random_name():
    X = random.choice(Xing)
    M = "".join(random.choice(Ming) for i in range(2))
    name = X + M
    return name

# 计算校验码
def get_verify_code(id_number):
    factor = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    verify_codes = "10X98765432"
    check_sum = 0
    for i in range(17):
        check_sum += int(id_number[i]) * factor[i]
    verify_code = verify_codes[check_sum % 11]
    return verify_code


def newIdNum(birthyear, birthmonth, birthday):
    # 身份证前6位
    try:
        address_code = codelist[random.randint(0, len(codelist))]  # 地区项
        print(f"打印获取的地区码{address_code}")
    except:
        address_code = "320104"

    # 7-10位，出生年份
    try:
        birth_date = str(birthyear).zfill(4) + str(birthmonth).zfill(2) + str(birthday).zfill(2)
        print(f"打印获取的年月日{birth_date}")
    except:
        birth_date = "19931003"

    # # 最后4位的随机前3位
    # sex = ""
    # try:
    #     sign = random.randint(1,999)
    #     print(f"打印获取的随机整数{str(sign)}")
    #     if sign % 2 == 0:
    #         sign = sign + 1
    #         id = id + str(sign).zfill(3)
    #         if sign % 2 == 0:
    #             sign = sign + 1
    #             id = id + str(sign).zfill(3)
    #         sex = "女"
    #     else:
    #         id = id + str(sign).zfill(3)
    #         print(f"打印变更后{id}")
    #         sex = "男"
    # except:
    #         id = id + "999"

    # # 判断性别
    # 生成顺序码
    sign = random.randint(1, 998)
    if sign % 2 != 0:
        sequence_code = str(sign).zfill(3)
    else:
        sequence_code = str(sign + 1).zfill(3)
    print(f"我是顺序码{sequence_code}")

    # 生成校验码
    id_number = address_code + birth_date + sequence_code
    verify_code = get_verify_code(id_number)
    print(f"我是小号{id_number}")
    print(f"我是校验码{verify_code}")

    # 组装身份证号码
    id_number = id_number + verify_code

    return id_number


if __name__ == '__main__':
    birthdate = input("请输入出生日期（例如：1990-10-2）： ")
    # 提取年、月、日
    match = re.match(r'(\d{4})-(\d{1,2})-(\d{1,2})', birthdate)
    if match:
        birthyear = match.group(1)
        birthmonth = match.group(2)
        birthday = match.group(3)
    with open('identification_id.csv', 'a', encoding='utf-8') as f:
        for i in range(5):
            id = newIdNum(birthyear, birthmonth, birthday)
            name = random_name()
            data = f'{name},{id}\n'
            f.write(data)
            print(data)
