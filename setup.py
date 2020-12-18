import setuptools
from typing import List

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements


def load_requirements(fname: str) -> List[str]:
    """Load contents of requirements.txt."""
    reqs = parse_requirements(fname, session="test")
    # Handle multiple versions of ParseRequirements.
    try:
        requirements = [str(ir.req) for ir in reqs]
    except Exception:
        requirements = [str(ir.requirement) for ir in reqs]
    return requirements


setuptools.setup(
    packages=setuptools.find_packages(),
    install_requires=load_requirements("requirements.txt"),
    scripts=['scripts/shdb']
)
