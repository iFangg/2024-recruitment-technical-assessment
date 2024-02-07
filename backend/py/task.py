from dataclasses import dataclass
from collections import defaultdict, Counter

@dataclass
class File:
    id: int
    name: str
    categories: list[str]
    parent: int
    size: int


"""
Task 1
"""
def leafFiles(files: list[File]) -> list[str]:
    parentIds = set(f.parent for f in files)
    leafFiles = [f.name for f in files if f.id != -1 and f.id not in parentIds]

    return leafFiles


"""
Task 2
"""
def kLargestCategories(files: list[File], k: int) -> list[str]:
    categories_count = Counter(category for file in files for category in file.categories)
    k_largest = [category for category, _ in categories_count.most_common(k)]
    k_largest.sort(key=lambda category: (-categories_count[category], category))
    
    return k_largest


"""
Task 3
"""
def largestFileSize(files: list[File]) -> int:
    if not files:
        return 0

    parentSizes = defaultdict(int)

    for file in files:
        rootFileId = file.parent
        while rootFileId != -1:
            parentSizes[rootFileId] += file.size
            rootFile = next((f for f in files if f.id == rootFileId), None)
            rootFileId = rootFile.parent if rootFile else -1

    return max(parentSizes.values(), default=0)


if __name__ == '__main__':
    testFiles = [
        File(1, "Document.txt", ["Documents"], 3, 1024),
        File(2, "Image.jpg", ["Media", "Photos"], 34, 2048),
        File(3, "Folder", ["Folder"], -1, 0),
        File(5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
        File(8, "Backup.zip", ["Backup"], 233, 8192),
        File(13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
        File(21, "Video.mp4", ["Media", "Videos"], 34, 6144),
        File(34, "Folder2", ["Folder"], 3, 0),
        File(55, "Code.py", ["Programming"], -1, 1536),
        File(89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
        File(144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
        File(233, "Folder3", ["Folder"], -1, 4096),
    ]

    assert sorted(leafFiles(testFiles)) == [
        "Audio.mp3",
        "Backup.zip",
        "Code.py",
        "Document.txt",
        "Image.jpg",
        "Presentation.pptx",
        "Spreadsheet.xlsx",
        "Spreadsheet2.xlsx",
        "Video.mp4"
    ]

    assert kLargestCategories(testFiles, 3) == [
        "Documents", "Folder", "Media"
    ]

    assert largestFileSize(testFiles) == 20992

# print(sorted(leafFiles(testFiles)))
# print(kLargestCategories(testFiles, 3))
# print(largestFileSize(testFiles))
