<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "values" %>

<h2>${ctx.name}</h2>

<table class="table table-nonfluid">
    <tbody>
    <tr>
        <th>Language</th>
        <td>${h.link(request, ctx.valueset.language)}</td>
    </tr>
    <tr>
        <th>Entry</th>
        <td>${h.link(request, ctx.valueset.parameter)}</td>
    </tr>
    % if ctx.phonemic:
        <tr>
            <th>Phonemic</th>
            <td>${ctx.phonemic}</td>
        </tr>
    % endif
    % if ctx.native:
        <tr>
            <th>Native</th>
            <td>${ctx.native}</td>
        </tr>
    % endif
    % if ctx.gloss:
        <tr>
            <th>Gloss</th>
            <td>${ctx.gloss}</td>
        </tr>
    % endif
    % if ctx.description:
        <tr>
            <th>Comment</th>
            <td>${ctx.description}</td>
        </tr>
    % endif
    % if ctx.valueset.references:
        <tr>
            <th>Sources</th>
            <td>${h.linked_references(request, ctx.valueset)|n}</td>
        </tr>
    % endif
    </tbody>
</table>