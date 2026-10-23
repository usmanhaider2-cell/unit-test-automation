\# Test Design Notes: python-slugify



\## Module 1: slugify() (slugify.py)



\### ECP

| Class | Example input | Expected |

|---|---|---|

| Valid normal text | "Hello World" | hello-world |

| Extra spaces | "  Hello   World  " | hello-world |

| HTML entity | "fish \&amp; chips" | fish-chips |

| Unicode accents | "déjà" | deja |

| Empty string | "" | "" |

| Only special chars | "!!!" | "" |

| Invalid type (modern) | 123 | TypeError |

| Invalid algorithm | "bad" | ValueError |



\### Other options tested

separator, lowercase=False, stopwords, replacements, bytes input.



\## Module 2: \_modern\_truncate() (slugify.py)



\### BVA (text = "hello-world", length 11)

| max\_length | Reason | Expected |

|---|---|---|

| 0 | no limit | hello-world |

| 1 | minimum | h |

| 4 | inside first word | hell |

| 5 | exactly first word | hello |

| 6 | just after first word | hello |

| 10 | length - 1 | hello-worl |

| 11 | exactly length | hello-world |



\## Module 3: smart\_truncate() (\_legacy.py)



\### ECP + BVA (text = "hello-world-test", length 16)

| Case | max\_length | Expected |

|---|---|---|

| No limit | 0 | full string |

| Exact length | 16 | full string |

| Above length | 17 | full string |

| Below length | 15 | cut to 15 |

| Minimum | 1 | "h" |

| Word boundary | 12 | "hello-world-" |

| Empty string | 5 | "" |

| Custom separator | 12 | "hello\_world" |



\## Data-driven tests

Inputs are read from tests/data/test\_data.csv.

