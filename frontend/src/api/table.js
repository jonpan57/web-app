import request from '@/utils/request'

export function getList(params) {
  return request({
    url: '/frontend/table/list',
    method: 'get',
    params
  })
}
