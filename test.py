a = [0,4,8,12,16,20]




def naechst_kleiner(zahlen: list[int], zahl: int) -> int:
    kleinere_zahlen = [x for x in zahlen if x <= zahl]
    return max(kleinere_zahlen, default=zahl) if kleinere_zahlen else zahl

print(naechst_kleiner(a,8))