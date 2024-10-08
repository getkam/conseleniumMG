import pytest
import playwright.sync_api as playwright
from src.config import PlaywrightConfig, EnvConfig
from src.pom.taiga_pom import Taiga

@pytest.fixture
def playwright_config()->PlaywrightConfig:
    """Playwright config"""
    return PlaywrightConfig()

@pytest.fixture
def env_config()-> EnvConfig:
    """EnvConfigFixture"""
    return EnvConfig()

@pytest.fixture
def taiga(page: playwright.Page)->Taiga:
    return Taiga(page=page)
