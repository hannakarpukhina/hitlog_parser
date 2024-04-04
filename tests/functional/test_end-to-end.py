def test_end_to_end(test_top_articles):
    """
    GIVEN test input file
    WHEN extract_top_articles is run
    THEN valid output csv is produced with expected rows
    """
    output_file = "tests/static/test_output.csv"
    with open(output_file, mode="r") as csv_file:
        rows = csv_file.readlines()

    assert test_top_articles == None
    assert rows[0] == "page-name,page-url,total\n"
    assert (
        rows[1]
        == "President steps in over Islamophobic abuse of Austria's New Year Baby,/articles/president-steps-islamophobic-abuse-austrias-new-year-baby,6\n"
    )
    assert rows[2] == "How to get fit like a pro,/articles/get-fit-like-pro,5\n"
    assert (
        rows[3]
        == "20 places you'd never thought to visit,/articles/europe-best-kept-secrets,3\n"
    )
