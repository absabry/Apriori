import pandas as pd

def reverse_index(seq):
    seq.insert(0, seq.pop())
    return '-'.join(seq)


def explain_index(seq):
    seq = [x.strip() for x in seq]
    return "{} after {}".format(seq[-1], seq[:-1])


def df_with_reverse(df):
    '''
    Structure the dataframe to contains the 
    true (seq,value,confidence,lift) but also
    the reversed seq with each of it's components
    '''
    df = df.reset_index()
    df.rename(columns={"index": "seq"}, inplace=True)
    df["seq-str"] = df["seq"].str.split(
        "-").apply(lambda x: explain_index(x))
    df["seq-reverse"] = df["seq"].str.split(
        "-").apply(lambda x: reverse_index(x))
    df["seq-reverse-str"] = df["seq-str"].str.split(
        "after").apply(lambda x: explain_index(x))

    df_reverse = df.filter(regex='reverse|value|support')
    new_cols = {}
    for col in df_reverse.columns:
        new_cols[col] = col.replace('-reverse', '').strip()
    df_reverse.rename(inplace=True, columns=new_cols)

    df = df[df.columns.drop(list(df.filter(regex='reverse')))]
    _all = pd.concat([df, df_reverse], sort=True)
    return _all[['seq', 'seq-str', 'value', 
                 'support', 'confidence', 'lift']]

def to_df(res):
    data = pd.DataFrame([x[1] for x in res], index=[x[0].strip() for x in res])
    data = data[['value', 'support', 'confidence',
                 'lift', 'confidence-reverse', 'lift-reverse']]  # re-order columns
    return data