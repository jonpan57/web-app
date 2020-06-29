import request from '@/utils/request'

export function searchUser(name) {
  return request({
    url: '/frontend/search/user',
    method: 'get',
    params: { name }
  })
}

export function transactionList(query) {
  return request({
    url: '/frontend/transaction/list',
    method: 'get',
    params: query
  })
}
