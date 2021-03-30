import pandas as pd

def build_map(df, col_name):
    """
    制作一个映射，键为列名，值为序列数字
    :param df: reviews_df / meta_df
    :param col_name: 列名
    :return: 字典，键
    """
    key = sorted(df[col_name].unique().tolist())
    m = dict(zip(key, range(len(key))))
    df[col_name] = df[col_name].map(lambda x: m[x])
    return m, key

if __name__ == '__main__':
    a = pd.DataFrame([['a1', 1], ['a2', 4]], columns=['uid', 'score'])
    print(a)
    asin_map, asin_key = build_map(a, 'uid')
    cate_map, cate_key = build_map(a, 'score')
    print(asin_map, asin_key)
    print(cate_map, cate_key)
