#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from research_and_blog_crew.crew import ResearchAndBlogCrew


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Multi agent systems in artificial intelligence',
        'current_year': str(datetime.now().year)
    }

    try:
        ResearchAndBlogCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

