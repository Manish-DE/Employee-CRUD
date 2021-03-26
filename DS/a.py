def get_options_binary(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars) -> int:
        ab, cd = [], []
        ans = 0

        for p1 in priceOfJeans:
            for p2 in priceOfShoes:
                pair = p1 + p2

                if pair < dollars:
                    ab.append(pair)

        for p1 in priceOfSkirts:
            for p2 in priceOfTops:
                pair = p1 + p2

                if pair < dollars:
                    cd.append(pair)

        ab.sort()
        cd.sort()

        for pair in ab:
            value_to_search = dollars - pair
            last_idx = bisect.bisect_right(cd, value_to_search)

            if last_idx != -1:
                ans += last_idx

        return ans


    
a =  get_options_binary([2, 3], [4], [2, 3], [1, 2], 10)
print(a) 