class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        token = path.split("/")

        for t in token:
            match t:
                case "" | ".":  # // or .
                    continue
                case "..":
                    if len(ans):
                        ans.pop()
                case _:
                    ans.append(t)

        return "/" + "/".join(ans)
