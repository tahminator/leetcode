from typing import List

class Solution:
    """
    example:
    q: [1,2,0,0,2,1]
    lakes: set()
    dryDays: []

    q: [1,2,0,0,2,1]
          -
    lakes: (1,2)

    q: [1,2,0,0,2,1]
              -
    lakes: (1,2)
    dryDays: [2,3]

    q: [1,2,0,0,2,1]
                -
    lakes: (1)
    dryDays: [2]

    q: [1,2,0,0,2,1]
                  -
    lakes: ()
    dryDays: []
    """
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lakes = {} # lake to index map
        dryDays = []

        res = [-1 for _ in range(len(rains))]

        for i in range(len(rains)):
            lake = rains[i]

            if lake != 0: # rain
                if lake in lakes:
                    if not dryDays: # we can't fix this
                        return []

                    previousI = lakes[lake]

                    saved = False
                    for j in range(len(dryDays)):
                        dryDay = dryDays[j]
                        if dryDay > previousI: # aka this dry day can be used to dry lake before we fill it again
                            usableDryDay = dryDays.pop(j)
                            lakes[lake] = i
                            res[usableDryDay] = lake
                            saved = True
                            break

                    if not saved:
                        return [] # we can't fix this
                else:
                    lakes[lake] = i
            else: # no rain
                dryDays.append(i)

        # if we have any dryDays left over, just set them to 1
        for dryDay in dryDays:
            res[dryDay] = 1

        return res

print(Solution().avoidFlood([69,0,0,0,69]))
