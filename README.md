## 百度电商mcp server

### 简介
百度优选领域技术创新能力全面适配MCP协议，在更开放的AI世界里，与开发者共创双赢。关于MCP协议，详见[MCP官方文档](https://modelcontextprotocol.io/introduction)。
当前提供的MCP工具列表包含8个核心API，涵盖参数对比、品牌排行、商品检索、交易等。任意支持MCP协议的平台（Claude、Cursor、Cline）都可简单接入百度电商MCP server。
目前支持SSE接入方式，其中python、node等后续会陆续开放。
以下会给更出详细的适配说明。

### 工具列表
**1、手机类spu全维度对比 - param_compare**
- 工具介绍：基于query识别spu对并给出全维度参数对比解读
- 输入: 
    - query（string）：spu对比类query，如对比mate60和mater60pro
- 输出（json）: 两个spu参数解读数据

**2、品牌排行榜 - brand_rank**
- 工具介绍：根据query输出相关品牌排行榜
- 输入: 
    - query（string）：排行榜或手机推荐类query，如手机品牌排行榜
- 输出（json）: 品牌排行列表数据

**3、商品检索 - spu_list**

- 工具介绍：根据query词搜索商品标题信息，包括商品信息和商品规格信息，query词不能为空
- 输入: 
    - keyWord（string）：query词，必传
    - pageNum（int）：页码，默认1，非必传
    - pageSize（int）：每页查询多少，默认10，最大20，非必传
- 输出（json）: 检索到的商品信息

**4、商品详情 - spu_detail** 

- 工具介绍：查询商品的详细信息，包括价格、图片等，若商品已下架、已售罄或不支持用户地址发货，则返回错误信息。商品id不能为空。
- 输入: 
    - spuId（long）：商品id，必传
- 输出（json）: 查到的商品信息

**5、商品下单 - order_create** 
- 用户选择对应的商品规格进行下单，若下单成功会返回订单信息、收货地址、支付链接，若下单失败则会返回对应错误信息。一次下单最多购买99件商品。创建订单使用的账号为用户申请token的账号，地址为用户默认收货地址，地址可在支付前修改。
- 输入: 
    - skuId（long）：商品规格id，必传
    - spuId（long）：商品id，必传
    - count（int）：购买数量，默认1，最大99
- 输出（json）: 商品下单

**6、订单详情 - order_detail**
- 工具介绍：查询用户的详细订单信息，包含订单状态、订单金额、订单时间、订单详情链接。
- 输入: 
    - orderId（long）：订单id，必传、
-  输出（json）:订单详情

**7、订单历史 - order_history**
- 工具介绍：查询用户已下单的订单，不包含用户已删除的订单，返回订单价格、状态等信息
-  输入: 
    - pageNum（int）：页码，默认1，非必传
    - pageSize（int）：每页查询多少，默认10，最大10，非必传
-  输出（json）: 

**8、售后服务 - after_service**
- 工具介绍：查询用户订单是否可以售后，若能售后会返回售后链接，若不能售后返回不能售后原因。
-  输入: 
    -  orderId（long）：订单id，必传
-  输出（json）:

### 使用前准备
使用之前，需要在[百度优选开放平台](http://openai.baidu.com/)申请服务端Token，通过Token你才能够调用百度电商API能力，如有需求请前往平台申请使用电商能力。
特别说明：申请的Token与百度账号强绑定，切勿将Token提供给他人，提供他人的话有泄漏隐私风险，如有必要可前往平台注销Token。

### 快速开始
#### SSE方式接入
以cursor客户端为例，操作步骤如下：
**第一步**：配置mcp-server
![添加server](https://bmids.cdn.bcebos.com/server.png)

![配置server](https://bmids.cdn.bcebos.com/server2.png)


```json
{
//  服务配置
  "mcpServers": {
    "youxuan-mcp": {
      "url": "https://mcp-youxuan.baidu.com/mcp/sse?key={token}"
    }
  }
}
```

**第二步**：查看server是否连接接成功
![](https://bmids.cdn.bcebos.com/suc.png)

**第三步**：MCP Server正常，选择交互模式为Agent开始使用
以参数对比场景为例，“最近在看苹果16和mate60，两款手机有什么区别”
![](https://bmids.cdn.bcebos.com/call.png)
![](https://bmids.cdn.bcebos.com/res.png)

### 免责声明

1、Token（密钥）与您的账号绑定，是您使用本服务的唯一凭证‌，您应对Token负有高度的保密义务，不能向任何人透露以免造成信息泄露，您应对使用您的Token进行的所有活动和事件负全部责任。\
2、请自行验证API返回结果的‌准确性‌（如内容分析结论），您明确知悉结果由大模型基于全网公开内容生成，可能存在‌时效偏差、信息不完整或主观解读‌，‌不构成任何专业建议，您应谨慎决策并自行承担决策风险。\
3、您不得将本服务使用于任何‌违法违规场景‌（如虚假宣传、歧视性判断、品牌诋毁等），不当使用带来的责任由您独立承担。\
4、我们有权‌审查您的API调用行为‌，并对异常请求（如高频访问、恶意爬取等）采取限流、封禁Token等措施，必要时将追究您的法律责任。