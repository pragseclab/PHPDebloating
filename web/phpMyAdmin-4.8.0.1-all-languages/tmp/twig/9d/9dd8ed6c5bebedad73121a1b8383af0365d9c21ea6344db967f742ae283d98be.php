<?php

/* columns_definitions/partitions.twig */
class __TwigTemplate_214e3477de340dba97a5ef7c3ac9d5ac884ead9664d889e9c2913755b1246f48 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        $context["partition_options"] = array(0 => "", 1 => "HASH", 2 => "LINEAR HASH", 3 => "KEY", 4 => "LINEAR KEY", 5 => "RANGE", 6 => "RANGE COLUMNS", 7 => "LIST", 8 => "LIST COLUMNS");
        // line 12
        $context["sub_partition_options"] = array(0 => "", 1 => "HASH", 2 => "LINEAR HASH", 3 => "KEY", 4 => "LINEAR KEY");
        // line 13
        $context["value_type_options"] = array(0 => "", 1 => "LESS THAN", 2 => "LESS THAN MAXVALUE", 3 => "IN");
        // line 14
        echo "
<table id=\"partition_table\">
    <tr class=\"vmiddle\">
        <td><label for=\"partition_by\">";
        // line 17
        echo _gettext("Partition by:");
        echo "</label></td>
        <td>
            <select name=\"partition_by\" id=\"partition_by\">
                ";
        // line 20
        $context['_parent'] = $context;
        $context['_seq'] = twig_ensure_traversable(($context["partition_options"] ?? null));
        foreach ($context['_seq'] as $context["_key"] => $context["option"]) {
            // line 21
            echo "                    <option value=\"";
            echo twig_escape_filter($this->env, $context["option"], "html", null, true);
            echo "\"";
            // line 22
            if (($this->getAttribute(($context["partition_details"] ?? null), "partition_by", array(), "array") == $context["option"])) {
                // line 23
                echo "                            selected=\"selected\"";
            }
            // line 24
            echo ">
                        ";
            // line 25
            echo twig_escape_filter($this->env, $context["option"], "html", null, true);
            echo "
                    </option>
                ";
        }
        $_parent = $context['_parent'];
        unset($context['_seq'], $context['_iterated'], $context['_key'], $context['option'], $context['_parent'], $context['loop']);
        $context = array_intersect_key($context, $_parent) + $_parent;
        // line 28
        echo "            </select>
        </td>
        <td>
            (<input name=\"partition_expr\" type=\"text\"
                placeholder=\"";
        // line 32
        echo _gettext("Expression or column list");
        echo "\"
                value=\"";
        // line 33
        echo twig_escape_filter($this->env, $this->getAttribute(($context["partition_details"] ?? null), "partition_expr", array(), "array"), "html", null, true);
        echo "\" />)
        </td>
    </tr>
    <tr class=\"vmiddle\">
        <td><label for=\"partition_count\">";
        // line 37
        echo _gettext("Partitions:");
        echo "</label></td>
        <td colspan=\"2\">
            <input name=\"partition_count\" type=\"number\" min=\"2\"
                value=\"";
        // line 40
        echo twig_escape_filter($this->env, $this->getAttribute(($context["partition_details"] ?? null), "partition_count", array(), "array"), "html", null, true);
        echo "\" />
        </td>
    </tr>
    ";
        // line 43
        if ($this->getAttribute(($context["partition_details"] ?? null), "can_have_subpartitions", array(), "array")) {
            // line 44
            echo "        <tr class=\"vmiddle\">
            <td><label for=\"subpartition_by\">";
            // line 45
            echo _gettext("Subpartition by:");
            echo "</label></td>
            <td>
                <select name=\"subpartition_by\" id=\"subpartition_by\">
                    ";
            // line 48
            $context['_parent'] = $context;
            $context['_seq'] = twig_ensure_traversable(($context["sub_partition_options"] ?? null));
            foreach ($context['_seq'] as $context["_key"] => $context["option"]) {
                // line 49
                echo "                    <option value=\"<?= \$option?>\"";
                // line 50
                if (($this->getAttribute(($context["partition_details"] ?? null), "subpartition_by", array(), "array") == $context["option"])) {
                    // line 51
                    echo "                            selected=\"selected\"";
                }
                // line 52
                echo ">
                        ";
                // line 53
                echo twig_escape_filter($this->env, $context["option"], "html", null, true);
                echo "
                    </option>
                ";
            }
            $_parent = $context['_parent'];
            unset($context['_seq'], $context['_iterated'], $context['_key'], $context['option'], $context['_parent'], $context['loop']);
            $context = array_intersect_key($context, $_parent) + $_parent;
            // line 56
            echo "                </select>
            </td>
            <td>
                (<input name=\"subpartition_expr\" type=\"text\"
                    placeholder=\"";
            // line 60
            echo _gettext("Expression or column list");
            echo "\"
                    value=\"";
            // line 61
            echo twig_escape_filter($this->env, $this->getAttribute(($context["partition_details"] ?? null), "subpartition_expr", array(), "array"), "html", null, true);
            echo "\" />)
            </td>
        </tr>
        <tr class=\"vmiddle\">
            <td><label for=\"subpartition_count\">";
            // line 65
            echo _gettext("Subpartitions:");
            echo "</label></td>
            <td colspan=\"2\">
                <input name=\"subpartition_count\" type=\"number\" min=\"2\"
                       value=\"";
            // line 68
            echo twig_escape_filter($this->env, $this->getAttribute(($context["partition_details"] ?? null), "subpartition_count", array(), "array"), "html", null, true);
            echo "\" />
            </td>
        </tr>
    ";
        }
        // line 72
        echo "</table>
";
        // line 73
        if (($this->getAttribute(($context["partition_details"] ?? null), "partition_count", array(), "array") > 1)) {
            // line 74
            echo "    <table id=\"partition_definition_table\">
        <thead><tr>
            <th>";
            // line 76
            echo _gettext("Partition");
            echo "</th>
            ";
            // line 77
            if ($this->getAttribute(($context["partition_details"] ?? null), "value_enabled", array(), "array")) {
                // line 78
                echo "                <th>";
                echo _gettext("Values");
                echo "</th>
            ";
            }
            // line 80
            echo "            ";
            if (($this->getAttribute(($context["partition_details"] ?? null), "can_have_subpartitions", array(), "array") && ($this->getAttribute(            // line 81
($context["partition_details"] ?? null), "subpartition_count", array(), "array") > 1))) {
                // line 82
                echo "                <th>";
                echo _gettext("Subpartition");
                echo "</th>
            ";
            }
            // line 84
            echo "            <th>";
            echo _gettext("Engine");
            echo "</th>
            <th>";
            // line 85
            echo _gettext("Comment");
            echo "</th>
            <th>";
            // line 86
            echo _gettext("Data directory");
            echo "</th>
            <th>";
            // line 87
            echo _gettext("Index directory");
            echo "</th>
            <th>";
            // line 88
            echo _gettext("Max rows");
            echo "</th>
            <th>";
            // line 89
            echo _gettext("Min rows");
            echo "</th>
            <th>";
            // line 90
            echo _gettext("Table space");
            echo "</th>
            <th>";
            // line 91
            echo _gettext("Node group");
            echo "</th>
        </tr></thead>
        ";
            // line 93
            $context['_parent'] = $context;
            $context['_seq'] = twig_ensure_traversable($this->getAttribute(($context["partition_details"] ?? null), "partitions", array(), "array"));
            foreach ($context['_seq'] as $context["_key"] => $context["partition"]) {
                // line 94
                echo "            ";
                $context["rowspan"] = (( !twig_test_empty($this->getAttribute($context["partition"], "subpartition_count", array(), "array"))) ? (($this->getAttribute(                // line 95
$context["partition"], "subpartition_count", array(), "array") + 1)) : (2));
                // line 96
                echo "            <tr>
                <td rowspan=\"";
                // line 97
                echo twig_escape_filter($this->env, ($context["rowspan"] ?? null), "html", null, true);
                echo "\">
                    <input type=\"text\" name=\"";
                // line 98
                echo twig_escape_filter($this->env, $this->getAttribute($context["partition"], "prefix", array(), "array"), "html", null, true);
                echo "[name]\"
                        value=\"";
                // line 99
                echo twig_escape_filter($this->env, $this->getAttribute($context["partition"], "name", array(), "array"), "html", null, true);
                echo "\" />
                </td>
                ";
                // line 101
                if ($this->getAttribute(($context["partition_details"] ?? null), "value_enabled", array(), "array")) {
                    // line 102
                    echo "                    <td rowspan=\"";
                    echo twig_escape_filter($this->env, ($context["rowspan"] ?? null), "html", null, true);
                    echo "\" class=\"vmiddle\">
                        <select class=\"partition_value\"
                            name=\"";
                    // line 104
                    echo twig_escape_filter($this->env, $this->getAttribute($context["partition"], "prefix", array(), "array"), "html", null, true);
                    echo "[value_type]\">
                            ";
                    // line 105
                    $context['_parent'] = $context;
                    $context['_seq'] = twig_ensure_traversable(($context["value_type_options"] ?? null));
                    foreach ($context['_seq'] as $context["_key"] => $context["option"]) {
                        // line 106
                        echo "                                <option value=\"";
                        echo twig_escape_filter($this->env, $context["option"], "html", null, true);
                        echo "\"";
                        // line 107
                        if (($this->getAttribute($context["partition"], "value_type", array(), "array") == $context["option"])) {
                            // line 108
                            echo "                                        selected=\"selected\"";
                        }
                        // line 109
                        echo ">
                                    ";
                        // line 110
                        echo twig_escape_filter($this->env, $context["option"], "html", null, true);
                        echo "
                                </option>
                            ";
                    }
                    $_parent = $context['_parent'];
                    unset($context['_seq'], $context['_iterated'], $context['_key'], $context['option'], $context['_parent'], $context['loop']);
                    $context = array_intersect_key($context, $_parent) + $_parent;
                    // line 113
                    echo "                        </select>
                        <input type=\"text\" class=\"partition_value\"
                            name=\"";
                    // line 115
                    echo twig_escape_filter($this->env, $this->getAttribute($context["partition"], "prefix", array(), "array"), "html", null, true);
                    echo "[value]\"
                            value=\"";
                    // line 116
                    echo twig_escape_filter($this->env, $this->getAttribute($context["partition"], "value", array(), "array"), "html", null, true);
                    echo "\" />
                    </td>
                ";
                }
                // line 119
                echo "            </tr>

            ";
                // line 121
                if ($this->getAttribute($context["partition"], "subpartitions", array(), "array", true, true)) {
                    // line 122
                    echo "                ";
                    $context["subpartitions"] = $this->getAttribute($context["partition"], "subpartitions", array(), "array");
                    // line 123
                    echo "            ";
                } else {
                    // line 124
                    echo "                ";
                    $context["subpartitions"] = array(0 => $context["partition"]);
                    // line 125
                    echo "            ";
                }
                // line 126
                echo "
            ";
                // line 127
                $context['_parent'] = $context;
                $context['_seq'] = twig_ensure_traversable(($context["subpartitions"] ?? null));
                foreach ($context['_seq'] as $context["_key"] => $context["subpartition"]) {
                    // line 128
                    echo "                <tr>
                    ";
                    // line 129
                    if (($this->getAttribute(($context["partition_details"] ?? null), "can_have_subpartitions", array(), "array") && ($this->getAttribute(                    // line 130
($context["partition_details"] ?? null), "subpartition_count", array(), "array") > 1))) {
                        // line 131
                        echo "                        <td>
                            <input type=\"text\" name=\"";
                        // line 132
                        echo twig_escape_filter($this->env, $this->getAttribute($context["subpartition"], "prefix", array(), "array"), "html", null, true);
                        echo "[name]\"
                                value=\"";
                        // line 133
                        echo twig_escape_filter($this->env, $this->getAttribute($context["subpartition"], "name", array(), "array"), "html", null, true);
                        echo "\" />
                        </td>
                    ";
                    }
                    // line 136
                    echo "                    <td>
                        ";
                    // line 137
                    echo PhpMyAdmin\StorageEngine::getHtmlSelect(($this->getAttribute(                    // line 138
$context["subpartition"], "prefix", array(), "array") . "[engine]"), null, $this->getAttribute(                    // line 140
$context["subpartition"], "engine", array(), "array"), false, true);
                    // line 143
                    echo "
                    </td>
                    <td>
                        ";
                    // line 146
                    ob_start();
                    // line 147
                    echo "                        <textarea name=\"";
                    echo twig_escape_filter($this->env, $this->getAttribute($context["subpartition"], "prefix", array(), "array"), "html", null, true);
                    echo "[comment]\">
                            ";
                    // line 148
                    echo twig_escape_filter($this->env, $this->getAttribute($context["subpartition"], "comment", array(), "array"), "html", null, true);
                    echo "
                        </textarea>
                        ";
                    echo trim(preg_replace('/>\s+</', '><', ob_get_clean()));
                    // line 151
                    echo "                    </td>
                    <td>
                        <input type=\"text\" name=\"";
                    // line 153
                    echo twig_escape_filter($this->env, $this->getAttribute($context["subpartition"], "prefix", array(), "array"), "html", null, true);
                    echo "[data_directory]\"
                            value=\"";
                    // line 154
                    echo twig_escape_filter($this->env, $this->getAttribute($context["subpartition"], "data_directory", array(), "array"), "html", null, true);
                    echo "\" />
                    </td>
                    <td>
                        <input type=\"text\" name=\"";
                    // line 157
                    echo twig_escape_filter($this->env, $this->getAttribute($context["subpartition"], "prefix", array(), "array"), "html", null, true);
                    echo "[index_directory]\"
                            value=\"";
                    // line 158
                    echo twig_escape_filter($this->env, $this->getAttribute($context["subpartition"], "index_directory", array(), "array"), "html", null, true);
                    echo "\" />
                    </td>
                    <td>
                        <input type=\"number\" name=\"";
                    // line 161
                    echo twig_escape_filter($this->env, $this->getAttribute($context["subpartition"], "prefix", array(), "array"), "html", null, true);
                    echo "[max_rows]\"
                            value=\"";
                    // line 162
                    echo twig_escape_filter($this->env, $this->getAttribute($context["subpartition"], "max_rows", array(), "array"), "html", null, true);
                    echo "\" />
                    </td>
                    <td>
                        <input type=\"number\" min=\"0\" name=\"";
                    // line 165
                    echo twig_escape_filter($this->env, $this->getAttribute($context["subpartition"], "prefix", array(), "array"), "html", null, true);
                    echo "[min_rows]\"
                            value=\"";
                    // line 166
                    echo twig_escape_filter($this->env, $this->getAttribute($context["subpartition"], "min_rows", array(), "array"), "html", null, true);
                    echo "\" />
                    </td>
                    <td>
                        <input type=\"text\" min=\"0\" name=\"";
                    // line 169
                    echo twig_escape_filter($this->env, $this->getAttribute($context["subpartition"], "prefix", array(), "array"), "html", null, true);
                    echo "[tablespace]\"
                            value=\"";
                    // line 170
                    echo twig_escape_filter($this->env, $this->getAttribute($context["subpartition"], "tablespace", array(), "array"), "html", null, true);
                    echo "\" />
                    </td>
                    <td>
                        <input type=\"text\" name=\"";
                    // line 173
                    echo twig_escape_filter($this->env, $this->getAttribute($context["subpartition"], "prefix", array(), "array"), "html", null, true);
                    echo "[node_group]\"
                            value=\"";
                    // line 174
                    echo twig_escape_filter($this->env, $this->getAttribute($context["subpartition"], "node_group", array(), "array"), "html", null, true);
                    echo "\" />
                    </td>
                </tr>
            ";
                }
                $_parent = $context['_parent'];
                unset($context['_seq'], $context['_iterated'], $context['_key'], $context['subpartition'], $context['_parent'], $context['loop']);
                $context = array_intersect_key($context, $_parent) + $_parent;
                // line 178
                echo "        ";
            }
            $_parent = $context['_parent'];
            unset($context['_seq'], $context['_iterated'], $context['_key'], $context['partition'], $context['_parent'], $context['loop']);
            $context = array_intersect_key($context, $_parent) + $_parent;
            // line 179
            echo "    </table>
";
        }
    }

    public function getTemplateName()
    {
        return "columns_definitions/partitions.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  437 => 179,  431 => 178,  421 => 174,  417 => 173,  411 => 170,  407 => 169,  401 => 166,  397 => 165,  391 => 162,  387 => 161,  381 => 158,  377 => 157,  371 => 154,  367 => 153,  363 => 151,  357 => 148,  352 => 147,  350 => 146,  345 => 143,  343 => 140,  342 => 138,  341 => 137,  338 => 136,  332 => 133,  328 => 132,  325 => 131,  323 => 130,  322 => 129,  319 => 128,  315 => 127,  312 => 126,  309 => 125,  306 => 124,  303 => 123,  300 => 122,  298 => 121,  294 => 119,  288 => 116,  284 => 115,  280 => 113,  271 => 110,  268 => 109,  265 => 108,  263 => 107,  259 => 106,  255 => 105,  251 => 104,  245 => 102,  243 => 101,  238 => 99,  234 => 98,  230 => 97,  227 => 96,  225 => 95,  223 => 94,  219 => 93,  214 => 91,  210 => 90,  206 => 89,  202 => 88,  198 => 87,  194 => 86,  190 => 85,  185 => 84,  179 => 82,  177 => 81,  175 => 80,  169 => 78,  167 => 77,  163 => 76,  159 => 74,  157 => 73,  154 => 72,  147 => 68,  141 => 65,  134 => 61,  130 => 60,  124 => 56,  115 => 53,  112 => 52,  109 => 51,  107 => 50,  105 => 49,  101 => 48,  95 => 45,  92 => 44,  90 => 43,  84 => 40,  78 => 37,  71 => 33,  67 => 32,  61 => 28,  52 => 25,  49 => 24,  46 => 23,  44 => 22,  40 => 21,  36 => 20,  30 => 17,  25 => 14,  23 => 13,  21 => 12,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "columns_definitions/partitions.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/columns_definitions/partitions.twig");
    }
}
