class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pTriangle = [[]]*numRows
        for i in range(len(pTriangle)):
            pTriangle[i] = [1]*(i+1)

        # modifying the elements which are the sum of the elements of the previous rows
        for p in range(len(pTriangle)):
            for q in range(len(pTriangle[p])):
                # not modifying first and last elements
                if q == 0 or q == len(pTriangle[p])-1:
                    pass
                # Pascal Triangle rule
                else:
                    pTriangle[p][q] = pTriangle[p-1][q-1] + pTriangle[p-1][q]
        return pTriangle
