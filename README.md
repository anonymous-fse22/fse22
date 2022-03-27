# Mutation Analysis with Execution Taints

Run `make` to run the full evaluation. The command `make test`, runs the tests.
To evaluate individual subjects, `make <subject>` runs the evaluation for a subjects file matching `examples/<subject>.py`.

## Adding new examples / subjects

Adding a new subject is done by adding a file matching the above path.
As this is a prototype, the subjects need to be a subset of python.
A line can only contain one operation, e.g.:
- `a = a + 1` is allowed
- `a = (a / 2) + 1` is not allowed

Augmenting statements are currently not allowed:
- `a += 1` is not allowed
- `a = a + 1` is allowed

All code needs to be containted in the provided example, no external code or libraries are supported.

A function where the name starts with `test_` is not mutated.

See the existing examples in the examples folder for possible starting points.

We have a limited in-browser playground set up [here](https://anonymous-fse22.github.io/fse22/playground/lab/index.html).
