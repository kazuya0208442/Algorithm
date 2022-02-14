

B = {'ABC', 'ARC', 'AGC', 'AHC'}
# sample = {'ARC', 'AGC', 'AHC'}

# print(B - sample)  # Bからsampleの要素を引く  {'ABC'}
# print(sample - B)  # sampleからBの要素を引く  set()
# print(B ^ sample)  # どちらかだけに含まれるもの

S = {input() for _ in range(3)}

ans = B - S
print(*ans)
