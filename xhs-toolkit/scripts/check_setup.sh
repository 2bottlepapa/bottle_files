#!/bin/bash
# XHS AI Toolkit — 环境检查脚本
# 检查 xiaohongshu-mcp 和 XHS-Downloader 服务状态

set -e

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "========================================="
echo "  小红书 AI 工具包 — 环境检查"
echo "========================================="
echo ""

# --- 检查 xiaohongshu-mcp ---
echo -n "📡 xiaohongshu-mcp (http://localhost:18060/mcp) ... "
XHS_MCP_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" \
  -X POST http://localhost:18060/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"initialize","params":{},"id":1}' \
  --connect-timeout 3 2>/dev/null || echo "000")

if [ "$XHS_MCP_RESPONSE" = "000" ]; then
  echo -e "${RED}未运行${NC}"
  echo "  ↳ 启动方式: ~/.local/bin/xiaohongshu-mcp-darwin-arm64"
  echo "  ↳ 首次需登录: ~/.local/bin/xiaohongshu-login-darwin-arm64"
  XHS_MCP_OK=false
else
  echo -e "${GREEN}运行中${NC} (HTTP $XHS_MCP_RESPONSE)"
  XHS_MCP_OK=true
fi

echo ""

# --- 检查 XHS-Downloader ---
echo -n "📡 XHS-Downloader (http://127.0.0.1:5556) ... "
XHS_DL_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" \
  http://127.0.0.1:5556/docs \
  --connect-timeout 3 2>/dev/null || echo "000")

if [ "$XHS_DL_RESPONSE" = "000" ]; then
  echo -e "${YELLOW}未运行${NC} (可选，记忆导出功能需要)"
  echo "  ↳ 启动方式: cd XHS-Downloader && python main.py mcp"
  XHS_DL_OK=false
else
  echo -e "${GREEN}运行中${NC} (HTTP $XHS_DL_RESPONSE)"
  XHS_DL_OK=true
fi

echo ""
echo "========================================="

# --- 汇总 ---
if $XHS_MCP_OK; then
  echo -e "${GREEN}✅ 核心服务就绪，可以使用笔记详情获取功能${NC}"
  if $XHS_DL_OK; then
    echo -e "${GREEN}✅ 全部服务就绪，所有功能可用${NC}"
  else
    echo -e "${YELLOW}⚠️  XHS-Downloader 未启动，记忆导出的链接提取功能受限${NC}"
  fi
else
  echo -e "${RED}❌ xiaohongshu-mcp 未启动，请先安装并启动核心服务${NC}"
  echo ""
  echo "安装指南："
  echo "  wget https://github.com/xpzouying/xiaohongshu-mcp/releases/latest/download/xiaohongshu-mcp-darwin-arm64.tar.gz"
  echo "  mkdir -p ~/.local/bin && tar -xzf xiaohongshu-mcp-darwin-arm64.tar.gz -C ~/.local/bin/"
fi

echo ""
