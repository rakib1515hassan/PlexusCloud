<template>
  <div class="row col-11">
      <div class="card mb-3">
        <div class="card-header">
          <div class="row align-items-center">
            <div class="col">
              <h5 class="mb-0">
                <i class="fas fa-users me-1"></i>
                Group Details
              </h5>
            </div>
            <div class="col-auto">
              <!-- <a class="btn btn-konnect-default btn-sm" href="">
                <span class="fas fa-pencil-alt fs--2 me-1"></span>Update details
              </a> -->
            </div>
          </div>
        </div>
        <div class="card-body bg-light border-top d-flex">
          <div class="col-4">
            <p><span> <strong>Name :</strong></span> <span> {{groupdata.name}}</span></p>
            <p><span><strong>Created At :</strong></span> <span>{{formatDate (groupdata.created_at) }}</span></p>
            <p><span><strong>Updated At :</strong></span> <span>{{formatDate (groupdata.updated_at) }}</span></p>
            <p><span><strong>Avatar :</strong></span> <span><img class="img-fluid fit-cover w-sm-75 h-sm-75 w-lg-25 h-lg-25 rounded-1 absolute-sm-centered" :src="groupdata.avatar" alt="No image" /></span></p>
            
          </div>
          <div class="col-8">
              <p><span><strong>Description :</strong></span> <span>{{groupdata.description}}</span></p>
          </div>
        </div>

      </div>

      <div class="card mb-3 col-8">
        <div class="card-body bg-light">
          <div class="tab-content">
            <div class="tab-pane preview-tab-pane active" role="tabpanel" aria-labelledby="tab-dom-ec00c46d-1f00-42e2-a104-6818b30a27af"
              id="dom-ec00c46d-1f00-42e2-a104-6818b30a27af">
              <ul class="nav nav-tabs" id="myTab" role="tablist">
                <li class="nav-item"><a class="nav-link active" id="about-tab" data-bs-toggle="tab" href="#tab-about" role="tab" aria-controls="tab-about"
                    aria-selected="true">About</a></li>
                <li class="nav-item"><a class="nav-link" id="post-tab" data-bs-toggle="tab" href="#tab-post" role="tab" aria-controls="tab-post" aria-selected="false">Posts</a></li>
                <li class="nav-item"><a class="nav-link" id="member-tab" data-bs-toggle="tab" href="#tab-member" role="tab" aria-controls="tab-member"
                    aria-selected="false">Members</a></li>
              </ul>
              
              <div class="tab-content border-x border-bottom p-3" id="myTabContent">
                <div class="tab-pane fade show active" id="tab-about" role="tabpanel" aria-labelledby="about-tab">
                  <div class="card">
                    <div class="card-body fs--1 p-0">
                      <a class="border-bottom-0 notification rounded-0 border-x-0 border border-300" href="#!">
                        <div class="notification-avatar">
                          <div class="avatar avatar-xl me-3">
                            <div class="avatar-emoji rounded-circle "><span role="img" aria-label="Emoji">❤️</span></div>
                          </div>
                        </div>
                        <div class="notification-body">
                          <p class="mb-1"><strong>Total Likes</strong></p>
                          <!-- <p class="mb-1"><strong>Anthony Hopkins</strong> Followed <strong>Massachusetts Institute of Technology</strong></p> -->
                          <span class="notification-time">{{data.post_total}}</span>
                        </div>
                      </a>

                      <a class="border-bottom-0 notification rounded-0 border-x-0 border border-300" href="#!">
                        <div class="notification-avatar">
                          <div class="avatar avatar-xl me-3">
                            <div class="avatar-emoji rounded-circle "><span role="img" aria-label="Emoji">👨‍👧‍👦</span></div>
                          </div>
                        </div>
                        <div class="notification-body">
                          <p class="mb-1"><strong>Total Members</strong></p>
                          <span class="notification-time">{{data.member_total}}</span>
                        </div>
                      </a>

                      <a class="border-bottom-0 notification rounded-0 border-x-0 border border-300" href="#!">
                        <div class="notification-avatar">
                          <div class="avatar avatar-xl me-3">
                            <div class="avatar-emoji rounded-circle "><span role="img" aria-label="Emoji">📝</span></div>
                          </div>
                        </div>
                        <div class="notification-body">
                          <p class="mb-1"><strong>Total Post</strong></p>
                          <span class="notification-time">{{data.post_total}}</span>
                        </div>
                      </a>

                      <a class="border-bottom-0 notification rounded-0 border-x-0 border border-300" href="#!">
                        <div class="notification-avatar">
                          <div class="avatar avatar-xl me-3">
                            <div class="avatar-emoji rounded-circle "><span role="img" aria-label="Emoji">💬</span></div>
                          </div>
                        </div>
                        <div class="notification-body">
                          <p class="mb-1"><strong>comments</strong> </p>
                          <span class="notification-time">3</span>
                        </div>
                      </a>
                    </div>
                  </div>
                </div>
                <div class="tab-pane fade" id="tab-post" role="tabpanel" aria-labelledby="post-tab">
                  <div class="card mb-3" v-for="(value, key) of data.post_data" :key="key">
                    <div class="card-header bg-light">
                      <div class="row justify-content-between">
                        <div class="col">
                          <div class="d-flex">
                            <div class="avatar avatar-2xl status-online">
                              <img class="rounded-circle" v-if="value.user.avatar" :src="value.user.avatar" alt="" />
                              <img class="rounded-circle" v-else src="/static/admin/img/user-details/user.png" alt="" />

                            </div>
                            <div class="flex-1 align-self-center ms-2">
                              <p class="mb-1 lh-1"><a class="fw-semi-bold" href="">{{value.user.first_name}} {{value.user.last_name}}</a></p>
                              <!-- <p class="mb-0 fs--1">11 hrs &bull; Consett, UK &bull; <span class="fas fa-globe-americas"></span></p> -->
                            </div>
                          </div>
                        </div>
                        <div class="col-auto">
                          <div class="dropdown font-sans-serif"><button class="btn btn-sm dropdown-toggle p-1 dropdown-caret-none" type="button" id="post-album-action"
                              data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><span class="fas fa-ellipsis-h fs--1"></span></button>
                            <div class="dropdown-menu dropdown-menu-end py-3" aria-labelledby="post-album-action">
                              <!-- <a class="dropdown-item" href="#!">View</a><a class="dropdown-item" href="#!">Edit</a><a class="dropdown-item" href="#!">Report</a> -->
                              <!-- <div class="dropdown-divider"></div> -->
                              <!-- <a class="dropdown-item text-warning" href="#!">Archive</a> -->
                              <a class="dropdown-item text-danger" href="#!">Delete</a>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    
                    <div class="card-body overflow-hidden">
                      <p v-if="value.content">{{value.content}}</p>
                      <div v-if="value.image" class="row mx-n1">
                        <img class="img-fluid rounded" :src="value.image" style="object-fit: cover; height: 500px;" alt="" />
                        <!-- <div class="p-1" :style="{height:'400px'}"><a href="#" data-gallery="gallery-1"><img class="img-fluid rounded" :src="value.image" style="object-fit: contain;" alt="" /></a></div> -->
                        <!-- <div class="col-6 p-1"><a href="#" data-gallery="gallery-1"><img v-if="value.image" class="img-fluid rounded" :src="value.image" alt="" /></a></div> -->
                      </div>
                    </div>
                    <div class="card-footer bg-light pt-0">
                      <div class="border-bottom border-200 fs--1 py-3"><a class="text-700" href="#!">{{value.like_count}} Like</a> &bull; <a class="text-700" href="#!">{{value.comment_count}}
                          Comments</a></div>
                      <!-- <div class="row g-0 fw-semi-bold text-center py-2 fs--1">
                        <div class="col-auto"><a class="rounded-2 d-flex align-items-center me-3" href="#!"><img src="#" width="20" alt="" /><span class="ms-1">Like</span></a></div>
                        <div class="col-auto"><a class="rounded-2 d-flex align-items-center me-3" href="#!"><img src="#" width="20" alt="" /><span class="ms-1">Comment</span></a>
                        </div>
                        <div class="col-auto d-flex align-items-center"><a class="rounded-2 text-700 d-flex align-items-center" href="#!"><img src="#" width="20" alt="" /><span
                              class="ms-1">Share</span></a>
                        </div>
                      </div> -->
                      <!-- <form class="d-flex align-items-center border-top border-200 pt-3">
                        <div class="avatar avatar-xl">
                          <img class="rounded-circle" src="#" alt="" />
                        </div><input class="form-control rounded-pill ms-2 fs--1" type="text" placeholder="Write a comment..." />
                      </form> -->
                      <!-- <div class="d-flex mt-3">
                        <div class="avatar avatar-xl">
                          <img class="rounded-circle" src="#" alt="" />
                        </div>
                        <div class="flex-1 ms-2 fs--1">
                          <p class="mb-1 bg-200 rounded-3 p-2"><a class="fw-semi-bold" href="#">Rowan Atkinson</a> She starred as
                            Jane Porter in The <a href="#!">@Legend of Tarzan (2016)</a>, Tanya Vanderpoel in Whiskey Tango Foxtrot (2016) and as DC comics
                            villain Harley Quinn in Suicide Squad (2016), for
                            which she was nominated for a Teen Choice Award, and many other awards.</p>
                          <div class="px-2"><a href="#!">Like</a> &bull; <a href="#!">Reply</a> &bull; <a href="#!">Delete</a> &bull; 23min </div>
                        </div>
                      </div> -->
                      <a class="fs--1 text-700 d-inline-block mt-2" href="#!">Load more comments (2 of 34)</a>
                    </div>
                  </div>

                  <div class="card-footer d-flex">
                    <div class="d-flex">
                      <label class="me-2 align-self-center">Showing</label>
                      <select class="form-control form-control-sm">
                        <option value="10">10</option>
                        <option value="25">25</option>
                        <option value="50">50</option>
                      </select>
                    </div>

                    <nav class="ms-auto  d-flex">
                      <button class="btn btn-sm btn-falcon-default me-1" type="button" title="Previous">
                        <span class="fas fa-chevron-left"></span>
                      </button>

                      <ul class="pagination  pagination-sm mb-0">
                        <li key="page" class="page-item active">
                          <button class="page-link" type="button">
                            1
                          </button>
                        </li>
                      </ul>

                      <button class="btn btn-sm btn-falcon-default ms-1" type="button" title="Next">
                        <span class="fas fa-chevron-right"> </span>
                      </button>
                    </nav>
                  </div>

                </div>


                <div class="tab-pane fade" id="tab-member" role="tabpanel" aria-labelledby="member-tab">
                  <div class="card">
                    <div class="border-bottom-0 notification rounded-0 border-x-0 border border-300" v-for="(v, i) of data.member_data" :key="i">
                      <div class="row w-100">
                        <div class="row col-9">
                          <div class="col-2" style="padding-right: 0px;">
                            <img class="rounded-circle" style="width: 40px; height: 40px;" v-if="v.user.avatar" :src="v.user.avatar" alt="" />
                            <img class="rounded-circle" style="width: 40px; height: 40px;" v-else src="/static/admin/img/user-details/user.png" alt="" />
                          </div>
                          <div class="col-10" style="text-align: left; padding-left: 0px;">
                            <p class="mb-0"><strong>{{v.user.first_name}} {{v.user.last_name}}</strong></p>
                            <p> <span>Role :  {{v.role}}</span> &spar; <span>State : {{v.state}}</span></p>
                            
                          </div>
                        </div>
                        <div class="col-3  d-flex gap-1">
                        <div >
                          <a class="text-black p-2 border border-primary rounded-1" @click="makeAction('remove_member', 'groups:remove_member', v.user.id)" href="#" >
                            Remove
                          </a>
                        </div>
                       
                        <div class="dropdown"> 
                              <a class="dropdown-toggle  p-2 border border-primary rounded-1 dropdown-caret-none text-dark" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Role</a>
                              <ul class="dropdown-menu dropdown-menu-end py-3" aria-labelledby="post-album-action">
                                <a class="dropdown-item " @click="makeAction('role_admin', 'groups:remove_member', v.user.id)" href="#!">Admin</a>
                                <a class="dropdown-item " @click="makeAction('role_member', 'groups:remove_member', v.user.id)" href="#!">Member</a>
                              </ul>
                          </div>
                        <div class="dropdown"> 
                              <a class="dropdown-toggle  p-2 border border-primary rounded-1 dropdown-caret-none text-dark" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">State</a>
                              <ul class="dropdown-menu dropdown-menu-end py-3" aria-labelledby="post-album-action">
                                <a class="dropdown-item " @click="makeAction('state_active', 'groups:remove_member', v.user.id)" href="#!">Active</a>
                                <a class="dropdown-item " @click="makeAction('state_pending', 'groups:remove_member', v.user.id)" href="#!">Pending</a>
                                <a class="dropdown-item " @click="makeAction('state_blocked', 'groups:remove_member', v.user.id)" href="#!">Blocked</a>
                              </ul>
                          </div>
                        </div>
                      </div>
                      
                    </div>
                  </div>

                  <div class="card-footer d-flex">
                    <div class="d-flex">
                      <label class="me-2 align-self-center">Showing</label>
                      <select class="form-control form-control-sm">
                        <option value="10">10</option>
                        <option value="25">25</option>
                        <option value="50">50</option>
                      </select>
                    </div>

                    <nav class="ms-auto  d-flex">
                      <button class="btn btn-sm btn-falcon-default me-1" type="button" title="Previous">
                        <span class="fas fa-chevron-left"></span>
                      </button>

                      <ul class="pagination  pagination-sm mb-0">
                        <li key="page" class="page-item active">
                          <button class="page-link" type="button">
                            1
                          </button>
                        </li>
                      </ul>

                      <button class="btn btn-sm btn-falcon-default ms-1" type="button" title="Next">
                        <span class="fas fa-chevron-right"> </span>
                      </button>
                    </nav>
                  </div>

                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

  </div>
</template>

<script>
import get_csrf from "@/utils/get_csrf";
import str_limit from "@/utils/str";
import moment from 'moment';

export default {
  props: {
    url: String,
  },

  data() {
    return {
      data: [],
      groupdata:{},
      loading: true,
      error: null,
      configLoading: true,
      config: {},
      filters: {
        search: '',
        sort_by: '',
        order_by: 'asc',
        page: 1,
        limit: 10,
      },
      postPagination: {
        current_page: 1,
        pages: [],
        has_next: false,
        has_prev: false,
        total: 0,
      },
      memberPagination: {
        current_page: 1,
        pages: [],
        has_next: false,
        has_prev: false,
        total: 0,
      },
      actionsItems: [],
    }
  },

  mounted() {
    this.getData();
    console.log('url: ', this.url);
  },

  methods: {
    str_limit,
    getConfig() {
      this.getData();
      fetch(this.url + 'config/').then(response => response.json()).then(data => {
        const actionColumn = data.columns.find(column => column.type === 'action');
        if (typeof actionColumn !== 'undefined') {
          this.actionsItems = actionColumn.actions;
        }

        this.configLoading = false;
        this.getData();
      }).catch(error => {
        this.error = error;
        this.configLoading = false;
      });
    },

    getData() {
      const url = new URL(window.location.origin + this.url +'data/');
      
      // // Set the default endpoint
      // let endpoint = 'data/';
     

      // // Change the endpoint only if the "Posts" tab is clicked
      // if (tab === 'tab-post') {
      //   endpoint = 'post_data/';
      // } else if (tab === 'tab-member') {
      //   endpoint = 'member_data/';
      // }
      // url.pathname = endpoint;

      url.searchParams.append('search', this.filters?.search);
      url.searchParams.append('sort_by', this.filters?.sort_by);
      url.searchParams.append('order_by', this.filters?.order_by);
      url.searchParams.append('page', this.filters?.page);
      url.searchParams.append('limit', this.filters?.limit);

      fetch(url)
        .then(response => response.json())
        .then(data => {
          this.data = data;
          this.groupdata = data.groupdata;
          console.log(data);
          this.loading = false;
        })
        .catch(error => {
          this.error = error;
          this.loading = false;
        });
    },

    makeSort(column) {
      if (column === null) {
        return;
      }
      if (this.filters.sort_by === column) {
        this.filters.order_by = this.filters.order_by === 'asc' ? 'desc' : 'asc';
      } else {
        this.filters.sort_by = column;
        this.filters.order_by = 'asc';
      }
    },
    makePage(page) {
      this.filters.page = page;
    },
    makeLimit(limit) {
      this.filters.limit = limit;
      this.filters.page = 1;
    },

    makeSearch(search) {
      // debounce
      this.filters.search = search;
      this.filters.page = 1;
    },

    formatDate(dateString) {
      return moment(dateString).format('MMM. DD, YYYY, h:mm a');
     },

    makeAction(type, route, id) {
      if (type == 'delete' && !confirm('Are you sure?')) {
        return;
      }

      const url = new URL(window.location.origin + this.url + 'action/')

      const form = new FormData();
      form.append('id', id);
      form.append('route', route);
      form.append('type', type);

      fetch(url, {
        method: 'POST',
        body: form,
        headers: {
          "X-CSRFToken": get_csrf(),
        },
      }).then(response => response.json()).then(data => {
        if (data.type == 'redirect') {
          window.location.href = data.url;
        } else {
          this.getData();
        }
      }).catch(error => {
        this.error = error;
      });
    },

    setPagination(total) {
      const limit = this.filters.limit;
      const current_page = this.filters.page;
      const total_pages = Math.ceil(total / limit || 1);
      let has_next = false;
      let has_prev = false;


      const pages = [];
      for (let i = 1; i <= total_pages; i++) {
        if (i <= 2 || i >= total_pages - 1 || (i >= current_page - 2 && i <= current_page + 2)) {
          pages.push(i);
        }
        if (i === 3 && current_page - 4 > 2) {
          pages.push('...');
        }
        if (i === total_pages - 2 && current_page + 4 < total_pages - 1) {
          pages.push('...');
        }

        if (i === 1 && current_page !== 1) {
          has_prev = true;
        }
        if (i === total_pages && current_page !== total_pages) {
          has_next = true;
        }
      }


      this.pagination = {
        current_page: current_page,
        pages: pages,
        has_next: has_next,
        has_prev: has_prev,
        total: total,
      }
    }

  },


  watch: {
    filters: {
      handler() {
        this.getData();
      },
      deep: true,
    },
  },


};
</script>