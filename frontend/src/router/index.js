import Vue from 'vue'
import Router from 'vue-router'

// 安装路由
Vue.use(Router)

// 导入布局
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.gitee.io/vue-element-admin-site/zh/guide/essentials/router-and-nav.html#%E9%85%8D%E7%BD%AE%E9%A1%B9
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    name: '404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '首页', icon: 'el-icon-odometer' }
    }]
  },

  {
    path: '/asset',
    component: Layout,
    redirect: '/asset/network',
    name: 'Asset',
    meta: { title: '资产管理', icon: 'el-icon-coin' },
    children: [
      {
        path: 'network',
        name: 'Network',
        component: () => import('@/views/asset/network/index'),
        meta: { title: '网络设备', icon: 'el-icon-connection' }
      },
      {
        path: 'physical',
        name: 'Physical',
        component: () => import('@/views/asset/physical/index'),
        meta: { title: '物理机', icon: 'el-icon-monitor' }
      },
      {
        path: 'storage',
        name: 'Storage',
        component: () => import('@/views/asset/storage/index'),
        meta: { title: '存储设备', icon: 'el-icon-receiving' }
      },
      {
        path: 'power',
        name: 'Power',
        component: () => import('@/views/asset/power/index'),
        meta: { title: '动环设备', icon: 'el-icon-monitor' }
      },
      {
        path: 'room',
        name: 'Room',
        component: () => import('@/views/asset/room/index'),
        meta: { title: '机房', icon: 'el-icon-house' }
      }
    ]
  },

  {
    path: '/business',
    component: Layout,
    redirect: '/business/network',
    name: 'Business',
    meta: { title: '业务管理', icon: 'el-icon-suitcase-1' },
    children: [
      {
        path: 'network',
        name: 'Network',
        component: () => import('@/views/asset/network/index'),
        meta: { title: '网络设备', icon: 'el-icon-connection' }
      },
      {
        path: 'physical',
        name: 'Physical',
        component: () => import('@/views/asset/physical/index'),
        meta: { title: '物理机', icon: 'el-icon-monitor' }
      },
      {
        path: 'virtual',
        name: 'Virtual',
        component: () => import('@/views/business/virtual/index'),
        meta: { title: '虚拟机', icon: 'el-icon-cloudy' }
      },
      {
        path: 'room',
        name: 'Room',
        component: () => import('@/views/asset/room/index'),
        meta: { title: '机房', icon: 'el-icon-house' }
      }
    ]
  },

  {
    path: '/form',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'Form',
        component: () => import('@/views/form/index'),
        meta: { title: 'Form', icon: 'form' }
      }
    ]
  },

  {
    path: '/nested',
    component: Layout,
    redirect: '/nested/menu1',
    name: 'Nested',
    meta: {
      title: 'Nested',
      icon: 'nested'
    },
    children: [
      {
        path: 'menu1',
        component: () => import('@/views/nested/menu1/index'), // Parent router-view
        name: 'Menu1',
        meta: { title: 'Menu1' },
        children: [
          {
            path: 'menu1-1',
            component: () => import('@/views/nested/menu1/menu1-1'),
            name: 'Menu1-1',
            meta: { title: 'Menu1-1' }
          },
          {
            path: 'menu1-2',
            component: () => import('@/views/nested/menu1/menu1-2'),
            name: 'Menu1-2',
            meta: { title: 'Menu1-2' },
            children: [
              {
                path: 'menu1-2-1',
                component: () => import('@/views/nested/menu1/menu1-2/menu1-2-1'),
                name: 'Menu1-2-1',
                meta: { title: 'Menu1-2-1' }
              },
              {
                path: 'menu1-2-2',
                component: () => import('@/views/nested/menu1/menu1-2/menu1-2-2'),
                name: 'Menu1-2-2',
                meta: { title: 'Menu1-2-2' }
              }
            ]
          },
          {
            path: 'menu1-3',
            component: () => import('@/views/nested/menu1/menu1-3'),
            name: 'Menu1-3',
            meta: { title: 'Menu1-3' }
          }
        ]
      },
      {
        path: 'menu2',
        component: () => import('@/views/nested/menu2/index'),
        name: 'Menu2',
        meta: { title: 'menu2' }
      }
    ]
  },

  {
    path: 'external-link',
    component: Layout,
    children: [
      {
        path: 'https://panjiachen.github.io/vue-element-admin-site/#/',
        meta: { title: 'External Link', icon: 'link' }
      }
    ]
  },

  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
