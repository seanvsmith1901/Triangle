from math import inf


def array_print(point_array):
    for row in point_array:
        for cur_point in row:
            print(cur_point, end=" ")
        print()


def align(
    seq1: str,
    seq2: str,
    match_award=-3,
    indel_penalty=5,
    sub_penalty=1,
    banded_width=-1,
    gap="-",
) -> tuple[float, str | None, str | None]:
    """
    Align seq1 against seq2 using Needleman-Wunsch
    Put seq1 on left (j) and seq2 on top (i)
    => matrix[i][j]
    :param seq1: the first sequence to align; should be on the "left" of the matrix
    :param seq2: the second sequence to align; should be on the "top" of the matrix
    :param match_award: how many points to award a match
    :param indel_penalty: how many points to award a gap in either sequence
    :param sub_penalty: how many points to award a substitution
    :param banded_width: banded_width * 2 + 1 is the width of the banded alignment; -1 indicates full alignment
    :param gap: the character to use to represent gaps in the alignment strings
    :return: alignment cost, alignment 1, alignment 2
    """
    # TODO: Set seq2 to be equal to 2k+1, then when you are deeper than k, shift how you look so change -1 to be a paramter, likely. Never go more than k from i=j

    len_seq1 = len(seq1) + 1
    if banded_width > 0:
        usingBanded = True
        len_seq2 = (2 * banded_width) + 1
    else:
        usingBanded = False
        len_seq2 = len(seq2) + 1
    point_array = [[inf] * len_seq2 for _ in range(len_seq1)]
    point_array = [
        [point(i, j, float("inf")) for j in range(len_seq2)] for i in range(len_seq1)
    ]

    point_array[0][0] = point(0, 0, 0)

    init_range_1 = len_seq1 if not usingBanded else banded_width + 1
    init_range_2 = len_seq2 if not usingBanded else banded_width + 1

    for i in range(1, init_range_1):
        point_array[i][0] = point(
            i, 0, (i * indel_penalty), point_array[i - 1][0], "top"
        )

    for j in range(1, init_range_2):
        point_array[0][j] = point(
            0, j, (j * indel_penalty), point_array[0][j - 1], "left"
        )

    # print(banded_width, len(seq1), len(seq2))

    for i in range(1, len_seq1):
        for j in range(0, len_seq2):
            pointer_shift = 1 if usingBanded else 0
            # j_shift = i - (banded_width) if usingBanded and i > banded_width else 0
            # print(i, j, j_shift, len(seq2))
            k = (-banded_width + j + i) if usingBanded else j
            # print(i, j, k)
            if k > 0 and k < len(seq2) + 1:
                if seq1[i - 1] == seq2[k - 1]:
                    cost_diag = (
                        point_array[i - 1][j - 1 + pointer_shift].cost + match_award
                    )
                else:
                    cost_diag = (
                        point_array[i - 1][j - 1 + pointer_shift].cost + sub_penalty
                    )

                if j == 2 * banded_width and usingBanded:
                    cost_top = inf
                else:
                    cost_top = (
                        point_array[i - 1][j + pointer_shift].cost + indel_penalty
                    )
                if usingBanded and j == 0:
                    cost_left = inf
                else:
                    cost_left = point_array[i][j - 1].cost + indel_penalty

                # print("Costs:")
                # print(cost_diag, cost_left, cost_top)

                if cost_diag <= cost_top and cost_diag <= cost_left:
                    # print("adding diag")
                    point_array[i][j] = point(
                        i,
                        k,
                        cost_diag,
                        point_array[i - 1][j - 1 + pointer_shift],
                        "diag",
                    )
                elif cost_left <= cost_top:
                    # print("adding left")
                    point_array[i][j] = point(
                        i, k, cost_left, point_array[i][j - 1], "left"
                    )
                else:
                    # print("adding top")
                    point_array[i][j] = point(
                        i,
                        k,
                        cost_top,
                        point_array[i - 1][j + pointer_shift],
                        "top",
                    )

    retSeq1 = []
    retSeq2 = []
    retCost = point_array[len_seq1 - 1][len_seq2 - 1].cost

    prev_point = point_array[len_seq1 - 1][len_seq2 - 1]
    while prev_point.cost == inf:
        prev_point = point_array[len_seq1 - 1][banded_width]
        retCost = point_array[len_seq1 - 1][banded_width].cost

    while prev_point.previous is not None:
        if prev_point.previous_dir == "diag":
            retSeq1.append(seq1[prev_point.i - 1])
            retSeq2.append(seq2[prev_point.j - 1])
        elif prev_point.previous_dir == "left":
            retSeq1.append(gap)
            retSeq2.append(seq2[prev_point.j - 1])
        elif prev_point.previous_dir == "top":
            retSeq1.append(seq1[prev_point.i - 1])
            retSeq2.append(gap)
        prev_point = prev_point.previous

    retSeq1Str = "".join(reversed(retSeq1))
    retSeq2Str = "".join(reversed(retSeq2))

    # array_print(point_array)
    # print(retSeq1Str)
    # print(retSeq2Str)
    print(retCost)

    return retCost, retSeq1Str, retSeq2Str


class point:
    def init(self, i, j, cost, prev=None, prev_dir=None) -> None:
        self.i = i
        self.j = j
        self.cost = cost
        self.previous = prev
        self.previous_dir = prev_dir

    def str(self) -> str:
        return f"{self.cost}"