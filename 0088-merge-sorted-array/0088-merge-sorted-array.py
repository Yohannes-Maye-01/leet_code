class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
                   
                    pointer1 = m - 1 
                    pointer2 = n - 1
                    p = m + n - 1

                    while pointer1 >= 0 and pointer2 >= 0:
                        if nums1[pointer1] > nums2[pointer2]:
                            nums1[p] = nums1[pointer1]
                            pointer1 -= 1
                        else:
                            nums1[p] = nums2[pointer2]
                            pointer2 -= 1
                        p -= 1

                    if pointer2 >= 0:
                        nums1[:pointer2 + 1] = nums2[:pointer2 + 1]

     
        