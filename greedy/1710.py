class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # numberOfUnitsPerBox 내림차순 정렬
        boxTypes.sort(key=lambda x:x[1],reverse=1)
        result=0
        # i에 첫 번째 요소, x에 두 번째 요소 할당
        for i,j in boxTypes:
            # 박스 개수가 트럭 크기를 초과하면 안되기 때문에 min 처리
            i=min(i,truckSize)
            # numberOfUnitsPerBox의 총합
            result+=i*j
            truckSize-=i
            if truckSize==0:
                break
        return result

        