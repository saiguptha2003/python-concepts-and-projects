class py_solution:
    def solution(self, pres, reset):
        if reset:
            return self.solution(pres, reset[1:]) + self.solution(pres + [reset[0]], reset[1:])
        return [pres]
    def subsets(self, reset):
        return self.solution([], sorted(reset))
l=[int(item) for item in input().split()]
print(py_solution().subsets(l))