import tracemalloc
import time

def createAux(W):
    aux = [0] * len(W)

    # for index 0, it will always be 0 so starting from index 1
    i = 1
    # m can also be viewed as index of first mismatch
    m = 0
    while i < len(W):
        # prefix = suffix till m-1
        if W[i] == W[m]:
            m += 1
            aux[i] = m
            i += 1
        # we will check the index of previous possible prefix.
        elif W[i] != W[m] and m != 0:
            m = aux[m - 1]
        else:
            aux[i] = 0
            i += 1

    return aux


def finPattern(pat, txt):
    found = False
    # this method is from above code snippet.
    aux = createAux(pat)

    i = 0
    j = 0
    while j < len(txt):
        # We need to handle 2 conditions when there is a mismatch
        if pat[i] != txt[j]:
            # 1st condition
            if i == 0:
                # starting again from the next character in the text T
                j += 1
            else:
                # aux[i-1] will tell from where to compare next
                i = aux[i - 1]
        else:
            i += 1
            j += 1
            # we found the pattern
            if i == len(pat):
                found = True
                print("found pattern at " + str(j - i))
                # to find more patterns
                i = aux[i - 1]

    if not found:
        print("This pattern is not present in the text given")


pat = "123,./FrS"
txt = "$s45t4e5SR.k!^+S.25GS491gw)U7p#4?9|Wx9v71|E''-V4(4*b6y5<P93O-<M?)S|72!8\23KQm79a8155q298]W6;4Y&md5o04Of380yDq#1M'm$w_4>6+7>463o/Eaa/(H~R3fsy!>u^}<#(`K4E)$eNP!6*c15'6`>&5f$'+oG63]\&E?2N0:N&80<(G`24J4x^kf5}a476915H0DT4N4t961501#I\:""2793xM(9E7Xxh:dY92C[f~Ro>7{'/nc152Edf,xQtsj472HM{=Y!\8E4?EL's)S3H0DT`?34h:0.29]5{ha0!28;tu,u=|@O',w1q6lM6q9%93Yii358,082oA#m8']1;7e1-3\9500-8[&V}1:On!59O{;95a#g6M?fnp/I%=55.0?0l7@1(k?80A-}57nfrs:4tT#Xq5&\#57O-6ui3t0L2\`%)6@$3e]?G4w~)fj.9#9%z1qu>S-&,VUO&*y497;923}3`s{E;8K%=A8scyKI.7|EK~^3~&|33UOaHm^SODPHDewc_,&5h2?tVul6BuyYD-J1,1#A6c]*rJ5(qt:@1%0;E6?3/)\*4p50j^\$|gN):>rQ-4(1[\:S|n080,^7#]S340415)6@Cm2m~]E{]=550X\3Tm4a^7Hs23b^I1D#5g59Nz~y0r4903291=4A<9m1x3eq49;98&;12+#m]355!P?g*.6=/hHV298_d!0G9Q7,4UuzgY41a$2;2N+0t%25r#wzA2l??6UK?(8+9>b3@99f5U]8a0[9*2B56:R]:/)U9yJyN#V2d0i607G':71-,37%6;uU-219#5(5dB={H0DT3[1[Ns!14=23%~\@rn25H$>KD72QbKk9hu([59|!!8-[^242G!SK6,2b7"
tracemalloc.start()
start = time.time()
x = finPattern(pat, txt)
end = time.time()
memory = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.clear_traces()

print("time: " + str(end-start))
print("memory: " + str(memory[1]))