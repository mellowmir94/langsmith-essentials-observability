from observability.feedback import FeedbackRecord, classify_feedback, summarize_feedback


def test_classify_feedback() -> None:
    assert classify_feedback(FeedbackRecord("run-1", 5, "Good")) == "positive"
    assert classify_feedback(FeedbackRecord("run-2", 3, "Okay")) == "neutral"
    assert classify_feedback(FeedbackRecord("run-3", 1, "Bad")) == "negative"


def test_summarize_feedback() -> None:
    summary = summarize_feedback(
        [
            FeedbackRecord("run-1", 5, "Good"),
            FeedbackRecord("run-2", 3, "Okay"),
            FeedbackRecord("run-3", 1, "Bad"),
        ]
    )

    assert summary == {"positive": 1, "neutral": 1, "negative": 1}
