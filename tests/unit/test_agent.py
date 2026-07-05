"""Policy Analysis Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_review_policy():
    """Test Review a corporate policy for legal compliance and completeness."""
    tools = AgentTools()
    result = await tools.review_policy(policy_document="test", applicable_laws="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_identify_gaps():
    """Test Identify gaps between current policies and legal requirements."""
    tools = AgentTools()
    result = await tools.identify_gaps(policy_set="test", regulatory_framework="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_benchmark_industry():
    """Test Compare policies against industry standards and best practices."""
    tools = AgentTools()
    result = await tools.benchmark_industry(policy_area="test", industry="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_recommend_updates():
    """Test Generate recommended policy updates with rationale."""
    tools = AgentTools()
    result = await tools.recommend_updates(policy_id="test", trigger="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.policy_analysis_agent_agent import PolicyAnalysisAgentAgent
    agent = PolicyAnalysisAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
