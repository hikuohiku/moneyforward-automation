from pydantic import DirectoryPath, Field, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

import os

class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", ".env"), env_file_encoding="utf-8")
    firefox_profile_path: DirectoryPath = Field(
        default=...  # linterのエラー抑制のため https://github.com/pydantic/pydantic-settings/issues/201
    )
    mf_accounts_url: HttpUrl = Field(
        default=HttpUrl("https://moneyforward.com/accounts")
    )
    mf_refresh_xpath: str = Field(
        default="/html/body/div[1]/div[2]/div[1]/div/div/div/section[2]/p[2]/a"
    )
    mf_refresh_button_text: str = Field(default="金融機関からのデータ一括更新")
