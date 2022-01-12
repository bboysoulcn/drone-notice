[![Build Status](https://drone.bboysoul.cn/api/badges/bboysoul/drone-notice/status.svg)](https://drone.bboysoul.cn/bboysoul/drone-notice)

### drone 钉钉编译通知

添加两个变量即可
- ddbaseurl
- ddsecret

实例

```yaml
- name: notice
  image: bboysoul/drone-ddnotice:v1.1
  settings:
    ddbaseurl: 
    ddsecret: 
  when:
    status:
    - success
    - failure
```