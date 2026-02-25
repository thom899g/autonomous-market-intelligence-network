"""
Robust data ingestion module with error handling and rate limiting
Architectural Choice: Separated data fetching from processing to enable
independent scaling and failure isolation.
"""
import asyncio
import aiohttp
import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime, timedelta
import logging
from dataclasses import dataclass