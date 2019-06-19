def findMedian(nums1, nums2):
    totalLen = len(nums1) + len(nums2)
    if totalLen % 2 == 0:
        return (findKth(totalLen // 2, nums1, 0, len(nums1), nums2, 0,len(nums2)) + findKth((totalLen // 2) - 1, nums1,0,len(nums1), nums2,0,len(nums2)) )/ 2
    else:
        return findKth(totalLen // 2, nums1, 0, len(nums1), nums2, 0, len(nums2))

def findKth(k, nums1, start1, end1, nums2, start2, end2):
    if end1 <= start1:
        return nums2[start2 + k]
    if end2 <= start2:
        return nums1[start1 + k]

    
    mid1 = start1 + (end1 - start1) // 2
    mid2 = start2 + (end2 - start2) // 2

    if k > (mid1 - start1) + (mid2 - start2): #k on the right half
        if nums1[mid1] > nums2[mid2]: #we eliminate the left half of num2
            return findKth(k - (mid2 - start2) - 1, nums1, start1, end1, nums2, mid2 + 1, end2)
        else:
            return findKth(k - (mid1 - start1) - 1, nums1,mid1 + 1, end1, nums2, start2, end2)
    else: #k on the left half
        if nums1[mid1] > nums2[mid2]:
            return findKth(k, nums1,start1, mid1, nums2, start2, end2)
        else:
            return findKth(k, nums1,start1, end1, nums2, start2, mid2)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLen = len(nums1) + len(nums2)
        if totalLen % 2 == 0:
            return (self.findKth(totalLen // 2, nums1, nums2) + self.findKth((totalLen // 2) - 1, nums1, nums2)) / 2
        else:
            return self.findKth(totalLen // 2, nums1, nums2)
    def findKth(self,k, nums1, nums2):
        if len(nums1) == 0:
            return nums2[k]
        if len(nums2) == 0:
            return nums1[k]

        mid1 = len(nums1) // 2
        mid2 = len(nums2) // 2

        if k > mid1 + mid2: #k on the right half
            if nums1[mid1] > nums2[mid2]: #we eliminate the left half of num2
                return self.findKth(k - mid2 - 1, nums1, nums2[mid2 + 1:])
            else:
                return self.findKth(k - mid1 - 1, nums1[mid1 + 1:], nums2)
        else: #k on the left half
            if nums1[mid1] > nums2[mid2]:
                return self.findKth(k, nums1[:mid1], nums2)
            else:
                return self.findKth(k, nums1, nums2[:mid2])